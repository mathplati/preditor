Previsão de Internações - Hospital Sabará

Este projeto foi desenvolvido para prever o número de internações no Hospital Sabará com base nas condições climáticas (temperatura e umidade) da cidade de São Paulo. O código utiliza dados da previsão do tempo da API OpenWeatherMap para gerar uma previsão de internações respiratórias e classificar essas internações por doenças, como bronquiolite, gripe, rinovírus, etc.

Funcionalidades

Previsão de Internações: O código gera uma previsão do número de internações para os próximos 5 dias.

Classificação das Internações: As internações são classificadas por doenças respiratórias, como bronquiolite, gripe, rinovírus, entre outras.

Análise Climática: O sistema analisa as condições climáticas (temperatura e umidade) para prever os riscos e padrões de internações.

Relatório Detalhado: O relatório inclui o resumo climático, o número médio de internações e uma classificação detalhada por doença.


Requisitos
Python 3.x

Biblioteca requests para obter os dados da API do OpenWeatherMap.

Biblioteca colorama para melhorar a exibição no terminal.

Como Usar
1. Instale as Dependências
Este código requer o Python 3.x. Você pode instalar as dependências necessárias executando o seguinte comando no terminal:

bash
Copiar
Editar
pip install requests colorama
2. Obtenha sua Chave de API do OpenWeatherMap
Você precisará de uma chave de API para acessar a previsão do tempo. Obtenha sua chave gratuita em OpenWeatherMap.

Depois de obter sua chave, substitua a variável API_KEY no código com a sua chave pessoal:

python
Copiar
Editar
API_KEY = "sua-chave-de-api"
3. Configuração da Cidade
O código está configurado para obter a previsão do tempo para a cidade de São Paulo. Se você deseja alterar a cidade, basta modificar a variável CITY no código para o nome da cidade e o código do país que você deseja:

python
Copiar
Editar
CITY = "São Paulo,br"
O formato da cidade deve ser "nome_da_cidade,código_do_país", onde o código do país é a abreviação de duas letras (por exemplo, "br" para Brasil, "us" para Estados Unidos, etc.).

4. Executando o Script
Para executar o código, basta rodar o script Python no terminal:

bash
Copiar
Editar
python previsao_internacoes.py
5. Relatório Gerado
Após executar o script, ele gerará um relatório com as previsões de internações para os próximos 5 dias. O relatório será exibido no terminal e também será salvo em um arquivo previsao_output.json no diretório onde o script foi executado.

O relatório conterá as seguintes informações:

Resumo Climático: Clima médio (quente, ameno, frio) e a umidade média para os próximos dias.

Internações Médias: Número médio de internações esperadas para os próximos dias.

Risco Geral: Classificação do risco com base nas condições climáticas (Alto ou Moderado).

Classificação das Internações por Doença: Classificação das internações por doenças respiratórias, como bronquiolite, gripe, rinovírus e outros.

Previsões Detalhadas por Dia: Previsões de internações para cada um dos próximos 5 dias, com explicação do motivo do risco (temperatura e umidade).

Estrutura do Código
Obter Previsão Climática: A função obter_previsao_5_dias busca as previsões de tempo para os próximos 5 dias usando a API do OpenWeatherMap.

Agrupar Dados por Dia: A função agrupar_por_dia organiza os dados climáticos de cada dia para calcular as médias de temperatura e umidade.

Gerar Dados de Internações: A função gerar_dados_internacoes gera dados fictícios para simular as internações.

Ajustar Internações com Base no Clima: A função ajustar_internacoes_por_clima ajusta o número de internações com base na temperatura e umidade.

Classificação das Internações: A função classificar_internacoes distribui as internações previstas entre as doenças respiratórias.

Gerar Resumo: A função gerar_resumo gera um resumo com base nas previsões de internações e condições climáticas.

Impressão do Relatório: A função imprimir_relatorio exibe o relatório no terminal e salva o arquivo JSON.

Exemplo de Saída
Ao executar o script, o terminal exibirá algo semelhante a isso:

yaml
Copiar
Editar
============================================================
     RESUMO DE INTERNAÇÕES - HOSPITAL SABARÁ (5 DIAS)
============================================================

🌤️ Resumo Climático:
Clima médio: Ameno (23.5ºC)
Umidade média: Moderada/baixa (63%)

🏥 Internações médias: 15
⚠️ Risco Geral: Moderado

🦠 Classificação das Internações por Doença Respiratória:
Bronquiolite: 5 internações
Gripe: 4 internações
Rinovírus: 3 internações
VSR: 3 internações

📅 Previsões detalhadas por dia:

📅 Data: 01/05/2025
🏥 Internações previstas: 16
⚠️ Risco: Moderado
🌡️ Motivo: Temp: 22ºC, Umidade: 60%
—————————————————————————————————————————————

📅 Data: 02/05/2025
🏥 Internações previstas: 14
⚠️ Risco: Moderado
🌡️ Motivo: Temp: 23ºC, Umidade: 65%
—————————————————————————————————————————————

...
O arquivo previsao_output.json também será gerado com o seguinte formato:

json
Copiar
Editar
{
    "previsoes": [
        {
            "data": "01/05/2025",
            "temperatura": 22.0,
            "umidade": 60,
            "internacoes_previstas": 16,
            "risco": "Moderado",
            "risco_cor": "\u001b[32m",
            "motivo": "Temp: 22ºC, Umidade: 60%"
        },
        {
            "data": "02/05/2025",
            "temperatura": 23.0,
            "umidade": 65,
            "internacoes_previstas": 14,
            "risco": "Moderado",
            "risco_cor": "\u001b[32m",
            "motivo": "Temp: 23ºC, Umidade: 65%"
        }
    ],
    "resumo": {
        "clima_resumo": "Ameno",
        "umidade_resumo": "Moderada/baixa",
        "media_temperatura": 23.5,
        "media_umidade": 63,
        "media_internacoes": 15,
        "risco_geral": "Moderado",
        "classificacao_internacoes": {
            "bronquiolite": 5,
            "gripe": 4,
            "rinovírus": 3,
            "VSR": 3
        }
    }
}
Contribuições
Se você deseja contribuir para este projeto, fique à vontade para fazer um fork e enviar pull requests. Qualquer sugestão de melhorias ou correções é bem-vinda!