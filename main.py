import os
import json
import random
import requests
from datetime import datetime, timedelta
from collections import defaultdict
from colorama import init, Fore

init(autoreset=True)

API_KEY = "4427daced99be72963253843e5e4c366"
CITY = "São Paulo,br"

usuarios = []

def obter_previsao_5_dias():
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric&lang=pt"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return resposta.json()["list"]
    except:
        return []

def agrupar_por_dia(dados_raw):
    agrupado = defaultdict(list)
    for entrada in dados_raw:
        data_str = entrada["dt_txt"].split(" ")[0]
        agrupado[data_str].append({
            "temperatura": entrada["main"]["temp"],
            "umidade": entrada["main"]["humidity"]
        })
    medias_por_dia = []
    for data, medidas in agrupado.items():
        temp_media = sum(m["temperatura"] for m in medidas) / len(medidas)
        umid_media = sum(m["umidade"] for m in medidas) / len(medidas)
        data_formatada = datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
        medias_por_dia.append({
            "data": data_formatada,
            "temperatura": round(temp_media, 1),
            "umidade": round(umid_media)
        })
    return medias_por_dia

def carregar_historico_de_arquivo(caminho="historico.txt"):
    try:
        with open(caminho, "r") as f:
            return json.load(f)
    except:
        return gerar_dados_internacoes()

def salvar_historico_em_arquivo(dados, caminho="historico.txt"):
    try:
        with open(caminho, "w") as f:
            json.dump(dados, f, indent=4)
    except:
        pass

def gerar_dados_internacoes():
    hoje = datetime.today()
    return [{"data": (hoje + timedelta(days=i)).strftime("%d/%m/%Y"), "internacoes": random.randint(5, 20)} for i in range(7)]

def ajustar_internacoes_por_clima(temp, umid):
    base = 12
    if temp < 18 and umid > 70:
        return base + random.randint(5, 10)
    elif temp > 30 and umid < 50:
        return base + random.randint(3, 7)
    elif 18 <= temp <= 25 and 50 <= umid <= 70:
        return base
    else:
        return base + random.randint(2, 5)

def preparar_dados(clima, historico):
    media = sum(item["internacoes"] for item in historico) / len(historico)
    return {
        "media_internacoes": media,
        "temperatura": clima["temperatura"],
        "umidade": clima["umidade"],
        "data": clima["data"]
    }

def prever_internacoes(dados):
    temp = dados["temperatura"]
    umid = dados["umidade"]
    previsao = ajustar_internacoes_por_clima(temp, umid)
    if temp < 18 and umid > 70:
        risco, cor = "Alto", Fore.RED
    elif temp > 30 and umid < 50:
        risco, cor = "Moderado", Fore.YELLOW
    else:
        risco, cor = "Baixo", Fore.GREEN
    return {
        "data": dados["data"],
        "temperatura": temp,
        "umidade": umid,
        "internacoes_previstas": previsao,
        "risco": risco,
        "risco_cor": cor,
        "motivo": f"Temp: {temp}ºC, Umidade: {umid}%"
    }

def classificar_internacoes(qtd):
    dist = {"bronquiolite": 0.35, "gripe": 0.25, "rinovírus": 0.20, "VSR": 0.20}
    return {k: int(qtd * v) for k, v in dist.items()}

def gerar_resumo(previsoes):
    t = [p["temperatura"] for p in previsoes]
    u = [p["umidade"] for p in previsoes]
    i = [p["internacoes_previstas"] for p in previsoes]
    clima = "Frio" if sum(t)/len(t) < 18 else "Ameno" if sum(t)/len(t) <= 25 else "Quente"
    umid = "Alta" if sum(u)/len(u) > 70 else "Moderada/baixa"
    risco = "Alto" if any(p["risco"] == "Alto" for p in previsoes) else "Moderado"
    return {
        "clima_resumo": clima,
        "umidade_resumo": umid,
        "media_temperatura": round(sum(t)/len(t), 1),
        "media_umidade": round(sum(u)/len(u), 1),
        "media_internacoes": round(sum(i)/len(i)),
        "risco_geral": risco,
        "classificacao_internacoes": classificar_internacoes(int(sum(i)/len(i)))
    }

def imprimir_relatorio(previsoes, resumo):
    print("\n" + "=" * 60)
    print(f"{Fore.CYAN}RESUMO DE INTERNAÇÕES - HOSPITAL SABARÁ")
    print("=" * 60)
    print(f"\nClima: {resumo['clima_resumo']} ({resumo['media_temperatura']}ºC)")
    print(f"Umidade: {resumo['umidade_resumo']} ({resumo['media_umidade']}%)")
    print(f"Internações médias: {resumo['media_internacoes']}")
    print(f"Risco Geral: {resumo['risco_geral']}")
    for d, q in resumo['classificacao_internacoes'].items():
        print(f"{d.capitalize()}: {q} internações")
    print("\nDetalhes por dia:")
    for p in previsoes:
        print(f"\n{p['data']}")
        print(f"Internações previstas: {p['internacoes_previstas']}")
        print(f"Risco: {p['risco_cor']}{p['risco']}")
        print(f"Motivo: {p['motivo']}")
        print("-" * 40)

def salvar_previsoes(previsoes, resumo):
    try:
        with open("previsao_output.json", "w", encoding="utf-8") as f:
            json.dump({"previsoes": previsoes, "resumo": resumo}, f, indent=4, ensure_ascii=False)
    except:
        pass

def cadastrar_usuario():
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    usuarios.append({"nome": nome, "cpf": cpf, "telefone": telefone})
    salvar_usuarios()
    print("Cadastro realizado com sucesso!")

def salvar_usuarios():
    try:
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
    except:
        pass

def carregar_usuarios():
    global usuarios
    try:
        with open("usuarios.json", "r", encoding="utf-8") as f:
            usuarios = json.load(f)
    except:
        usuarios = []

def listar_usuarios():
    if not usuarios:
        print("Nenhum paciente cadastrado.")
        return
    print("\nPacientes cadastrados:")
    for u in usuarios:
        print(f"- {u['nome']} | CPF: {u['cpf']} | Tel: {u['telefone']}")

def menu():
    carregar_usuarios()
    while True:
        print("\n" + "=" * 50)
        print(f"{Fore.CYAN}{' MENU DO SISTEMA DE PREVISÃO ':^50}")
        print("=" * 50)
        print(f"{Fore.YELLOW}1.{Fore.RESET} Ver previsão geral")
        print(f"{Fore.YELLOW}2.{Fore.RESET} Ver previsão de um dia específico")
        print(f"{Fore.YELLOW}3.{Fore.RESET} Cadastrar novo histórico de internações")
        print(f"{Fore.YELLOW}4.{Fore.RESET} Cadastrar paciente")
        print(f"{Fore.YELLOW}5.{Fore.RESET} Listar pacientes cadastrados")
        print(f"{Fore.YELLOW}6.{Fore.RESET} Sair do sistema")
        print("=" * 50)
        op = input(f"{Fore.CYAN}Escolha uma opção: {Fore.RESET}")

        if op == "1":
            raw = obter_previsao_5_dias()
            if raw:
                dias = agrupar_por_dia(raw)
                hist = carregar_historico_de_arquivo()
                previsoes = [prever_internacoes(preparar_dados(d, hist)) for d in dias]
                resumo = gerar_resumo(previsoes)
                salvar_previsoes(previsoes, resumo)
                imprimir_relatorio(previsoes, resumo)
            else:
                print("Erro ao obter dados da previsão.")

        elif op == "2":
            raw = obter_previsao_5_dias()
            if raw:
                dias = agrupar_por_dia(raw)
                for idx, d in enumerate(dias):
                    print(f"{idx+1}. {d['data']}")
                try:
                    sel = int(input("Escolha o dia (número): ")) - 1
                    hist = carregar_historico_de_arquivo()
                    dados = preparar_dados(dias[sel], hist)
                    previsao = prever_internacoes(dados)
                    print(f"\nData: {previsao['data']}")
                    print(f"Internações previstas: {previsao['internacoes_previstas']}")
                    print(f"Risco: {previsao['risco_cor']}{previsao['risco']}")
                    print(f"Motivo: {previsao['motivo']}")
                except (ValueError, IndexError):
                    print("Opção inválida!")
            else:
                print("Erro ao obter dados da previsão.")

        elif op == "3":
            novo = []
            for i in range(7):
                dia = (datetime.today() + timedelta(days=i)).strftime("%d/%m/%Y")
                try:
                    val = int(input(f"Internações para {dia}: "))
                    novo.append({"data": dia, "internacoes": val})
                except ValueError:
                    print("Entrada inválida, usando valor padrão 10.")
                    novo.append({"data": dia, "internacoes": 10})
            salvar_historico_em_arquivo(novo)
            print("Histórico salvo com sucesso!")

        elif op == "4":
            cadastrar_usuario()

        elif op == "5":
            listar_usuarios()

        elif op == "6":
            print(f"{Fore.GREEN}Saindo do sistema... Até logo!")
            break

        else:
            print(f"{Fore.RED}Opção inválida! Tente novamente.")

        voltar = input("\nDigite 'M' para voltar ao menu ou 'S' para sair: ").strip().upper()
        if voltar == 'S':
            print(f"{Fore.GREEN}Saindo do sistema... Até logo!")
            break

if __name__ == "__main__":
    menu()
