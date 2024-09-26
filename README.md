# Análise Financeira com ROI e Magic Formula

Este projeto tem como objetivo realizar uma análise financeira de ações utilizando os indicadores ROI (Return on Investment) e a Magic Formula, para montar uma carteira de investimentos e verificar o desempenho da mesma em relação ao IBOVESPA

## Participantes do Projeto

- Luigi Ajello
    email: luigipedrosoajello@gmail.com
    LinkedIn: www.linkedin.com/in/luigi-pedroso-ajello-346934278
    GitHub:https://github.com/LuigiAjello
- Lucas Rodor
    email: lucasgomessr10@gmail.com
    Linkedin: www.linkedin.com/in/lucasrodor
    Github: https://github.com/lucasrodor
- Pedro Miranda 
    email: pedrocadaluz@gmail.com
    GitHub:https://www.linkedin.com/in/pedro-arthur-da-luz-miranda-4a94a5301/
    LinkedIn:https://github.com/pedrocadaluz

## Funcionalidades

- **Obtenção de dados via API**: Coleta de dados das ações e do Ibovespa de uma API externa.
- **Cálculo de rendimentos**: Cálculo do rendimento percentual das ações e do Ibovespa em determinado período.
- **Análise ROI**: Seleção das 10 ações com maior retorno sobre o investimento (ROI) e cálculo de rendimento da carteira.
- **Análise Magic Formula**: Seleção das 10 ações de acordo com a fórmula mágica de Joel Greenblatt, baseada nos indicadores ROIC (Return on Invested Capital) e Earning Yield e cálculo de rendimento da carteira.
- **Comparação com o Ibovespa**: Verificação do rendimento da carteira em comparação com o IBOVESPA no mesmo período e de cada ação da carteira.

## Modo de usar:
1- Acesse o site https://laboratoriodefinancas.com/home e faça seu cadastro para gerar o Token de acesso;
2- Copie o token e crie um arquivo .env e armazene essa informação dentro nele no formato: "TOKEN = 'seu token aqui'";
3- Selecione o período desejado de análise nos parâmetros das API's no arquivo api.py;
4- Rode o código e verifique a análise da carteira, ação e comparações.


## Pré-requisitos

- Python 3.11 ou superior
- Bibliotecas necessárias:
  - `requests`
  - `pandas`
  - `python-dotenv`
