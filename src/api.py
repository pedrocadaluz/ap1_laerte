import os
import requests
from dotenv import load_dotenv

# Carregar o token do arquivo .env
load_dotenv()
token = os.getenv('TOKEN')
headers = {'Authorization': f'JWT {token}'}

def obter_dados_planilhao(data_base):
    """Função para obter os dados do planilhão."""
    params = {'data_base': data_base}
    response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao', params=params, headers=headers)
    return response.json()["dados"] if response.status_code == 200 else None

def obter_preco_acoes(ticker, data_ini, data_fim):
    """Função para obter os dados de preço de ações."""
    params = {'ticker': ticker, 'data_ini': data_ini, 'data_fim': data_fim}
    response = requests.get('https://laboratoriodefinancas.com/api/v1/preco-corrigido', params=params, headers=headers)
    return response.json()["dados"] if response.status_code == 200 else None

def obter_preco_ibovespa(data_ini, data_fim):
    """Função para obter os dados do IBOVESPA."""
    params = {'ticker': 'ibov', 'data_ini': data_ini, 'data_fim': data_fim}
    response = requests.get('https://laboratoriodefinancas.com/api/v1/preco-diversos', params=params, headers=headers)
    return response.json()['dados'] if response.status_code == 200 else None
