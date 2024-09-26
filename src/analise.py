import re
import pandas as pd
from src.api import obter_preco_acoes, obter_preco_ibovespa
from src.utils import calcular_rendimento

def analisar_acoes(df_acoes, data_ini, data_fim):
    """Função para analisar o rendimento das ações."""
    resultados = []
    for ticker in df_acoes['ticker'].unique():  # Garantir que cada ticker seja analisado apenas uma vez
        dados_preco = obter_preco_acoes(ticker, data_ini, data_fim)
        if dados_preco:
            df_preco = pd.DataFrame(dados_preco)
            rendimento = calcular_rendimento(df_preco)
            resultados.append((ticker, rendimento))
        else:
            resultados.append((ticker, None))
    return resultados

def comparar_rendimentos(rendimentos, rendimento_ibov):
    """Função para comparar os rendimentos com o Ibovespa."""
    acima = [ticker for ticker, rend in rendimentos if rend is not None and rend > rendimento_ibov]
    abaixo = [ticker for ticker, rend in rendimentos if rend is not None and rend <= rendimento_ibov]
    return acima, abaixo
