# Previsão de Internações Respiratórias – Hospital Sabará

> Este é um sistema simples, feito para rodar no terminal, que ajuda a prever quantas crianças podem ser internadas por doenças respiratórias com base na previsão do tempo dos próximos dias. Ele também permite cadastrar pacientes.

---

## ✨ Funcionalidades (Menu)

| Opção                                     | O que faz                                                                                           |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **1 – Ver previsão geral**                | Mostra a previsão do tempo e a quantidade estimada de internações para os próximos 5 dias.          |
| **2 – Ver previsão de um dia específico** | Permite escolher um dia e ver a previsão de internações para esse dia.                              |
| **3 – Cadastrar novo histórico**          | Permite digitar quantas internações aconteceram nos últimos dias, para o sistema aprender com isso. |
| **4 – Cadastrar paciente**                | Salva os dados (nome, CPF e telefone) de um paciente em um arquivo.                                 |
| **5 – Listar pacientes**                  | Mostra todos os pacientes cadastrados até agora.                                                    |
| **6 – Sair**                              | Fecha o programa.                                                                                   |

---

## 🗂️ Arquivos do Projeto

```
previsao-internacoes/
├── main.py                # Código principal
├── historico.txt          # Internações informadas pelo usuário
├── usuarios.json          # Lista de pacientes cadastrados
├── previsao_output.json   # Relatório com previsão gerada
└── README.md              # Instruções e explicações
```

---

## ⚙️ O que você precisa para rodar

1. **Python 3.8 ou mais recente**
2. Uma conta gratuita no site [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)

   * Após se cadastrar, você receberá uma "API Key", que é como uma senha para acessar a previsão do tempo.

### Bibliotecas Python usadas

* `requests` → para acessar a previsão do tempo
* `colorama` → para deixar o menu colorido no terminal

---

## 🛠️ Como instalar e rodar o sistema

### 1. Baixe os arquivos do projeto

Você pode clicar em “Baixar ZIP” aqui no GitHub, ou usar o comando abaixo se souber usar o Git:

```bash
git clone <url-do-projeto>
cd previsao-internacoes
```

### 2. Instale as bibliotecas necessárias

Abra o terminal ou prompt de comando e digite:

```bash
pip install requests colorama
```

### 3. Configure a chave da previsão do tempo

Você pode colar sua chave no código `main.py`, assim:

```python
API_KEY = "SUA_CHAVE_AQUI"
```

Ou, se souber usar, pode configurar como variável de ambiente:

```bash
export OWM_KEY="SUA_CHAVE_AQUI"
```

---

## ▶️ Como abrir o programa

Digite no terminal:

```bash
python main.py
```

Você verá este menu:

```
============= MENU DO SISTEMA DE PREVISÃO =============
1. Ver previsão geral
2. Ver previsão de um dia específico
3. Cadastrar novo histórico de internações
4. Cadastrar paciente
5. Listar pacientes cadastrados
6. Sair do sistema
=======================================================
```

Depois de executar qualquer opção, você poderá escolher se quer voltar ao menu ou sair.

---

## 🔍 Visão geral das partes do sistema

```python
obter_previsao_5_dias()  # Pega a previsão de 5 dias
agrupar_por_dia()        # Organiza as previsões por data
prever_internacoes()     # Estima número de internações
menu()                   # Mostra e executa o menu
```

---

## 📦 Dica: salvar as dependências

Se quiser compartilhar o projeto com alguém:

```bash
pip freeze > requirements.txt
```

A pessoa que receber pode instalar tudo com:

```bash
pip install -r requirements.txt
```

---

## ❓ Dúvidas comuns

**Preciso saber programar para usar?**
Não! Basta seguir o passo a passo acima.

**Posso usar no Windows?**
Sim, funciona no Windows, Linux e Mac.

**Onde vejo os pacientes que cadastrei?**
No arquivo `usuarios.json` (abre com qualquer editor de texto).

---

## 🛡️ Licença

Este projeto é acadêmico, sem fins lucrativos. MIT © 2025
