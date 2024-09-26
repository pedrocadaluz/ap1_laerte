import pandas as pd
import re
from src.api import obter_dados_planilhao, obter_preco_ibovespa
from src.analise import analisar_acoes, comparar_rendimentos
from src.utils import calcular_rendimento

def main():
    # Executando a análise
    dados_planilhao = obter_dados_planilhao('2023-04-03')
    df_planilhao = pd.DataFrame(dados_planilhao)

    # API IBOVESPA
    dados_ibovespa = obter_preco_ibovespa('2023-04-01', '2024-04-01')
    df_ibovespa = pd.DataFrame(dados_ibovespa)

    # Calcular rendimento do IBOVESPA
    rendimento_ibovespa = calcular_rendimento(df_ibovespa)

    # Análise ROI
    df_roe = df_planilhao[['ticker', 'roe', 'volume']].copy()
    df_roe['nome_base'] = df_roe['ticker'].apply(lambda x: re.sub(r'\d+$', '', x))
    df_roe_filtrado = df_roe.loc[df_roe.groupby('nome_base')['volume'].idxmax()].copy()
    df_top_10_roi = df_roe_filtrado[['ticker', 'roe']].sort_values(by='roe', ascending=False).head(10)

    rendimentos_roi = analisar_acoes(df_top_10_roi, '2023-04-03', '2024-04-01')
    acima_ibov_roi, abaixo_ibov_roi = comparar_rendimentos(rendimentos_roi, rendimento_ibovespa)

    # Análise Magic Formula
    df_magic = df_planilhao[['setor', 'ticker', 'roic', 'earning_yield', 'volume']].copy()

    # Extrair o nome base da ação
    df_magic['nome_base'] = df_magic['ticker'].apply(lambda x: re.sub(r'\d+$', '', x))

    # Filtrar ações repetidas, mantendo a de maior volume
    df_magic_filtrado = df_magic.loc[df_magic.groupby('nome_base')['volume'].idxmax()].copy()

    # Remover setores que não se aplicam à fórmula
    setores_remover = ['banco', 'seguro', 'financeiro']
    df_magic_filtrado = df_magic_filtrado.loc[~df_magic_filtrado['setor'].isin(setores_remover)].copy()

    # Remover empresas com dados faltantes em 'roic' ou 'earning_yield'
    df_magic_filtrado = df_magic_filtrado.dropna(subset=['roic', 'earning_yield'])

    # Calcular rankings individuais
    df_magic_filtrado['ranking_roic'] = df_magic_filtrado['roic'].rank(ascending=False)
    df_magic_filtrado['ranking_earning_yield'] = df_magic_filtrado['earning_yield'].rank(ascending=False)

    # Calcular ranking combinado
    df_magic_filtrado['ranking_combined'] = df_magic_filtrado['ranking_roic'] + df_magic_filtrado['ranking_earning_yield']

    # Selecionar top 10 ações com base no ranking combinado
    df_magic_top10 = df_magic_filtrado.sort_values(by='ranking_combined').head(10)

    # Analisar rendimentos das ações selecionadas
    rendimentos_mf = analisar_acoes(df_magic_top10, '2023-04-03', '2024-04-01')
    acima_ibov_mf, abaixo_ibov_mf = comparar_rendimentos(rendimentos_mf, rendimento_ibovespa)

    # Exibindo resultados
    print(f"Rendimento Ibovespa = {rendimento_ibovespa:.2f}%")
    print("---------------------------------------------------")
    print("ROI:")
    for ticker, rendimento in rendimentos_roi:
        if rendimento is not None:
            print(f"Rendimento total da ação {ticker}: {rendimento:.2f}%")
    carteira_roi = sum([r for _, r in rendimentos_roi if r is not None]) / len(rendimentos_roi)  # Média ponderada
    print(f"Rendimento carteira ROI = {carteira_roi:.2f}%")
    print(f"Ações acima do Ibovespa: {acima_ibov_roi}")
    print(f"Ações abaixo do Ibovespa: {abaixo_ibov_roi}")
    print("---------------------------------------------------")
    print("Magic Formula:")
    for ticker, rendimento in rendimentos_mf:
        if rendimento is not None:
            print(f"Rendimento total da ação {ticker}: {rendimento:.2f}%")
    carteira_mf = sum([r for _, r in rendimentos_mf if r is not None]) / len(rendimentos_mf)  # Média ponderada
    print(f"Rendimento carteira Magic Formula = {carteira_mf:.2f}%")
    print(f"Ações acima do Ibovespa: {acima_ibov_mf}")
    print(f"Ações abaixo do Ibovespa: {abaixo_ibov_mf}")
    print("---------------------------------------------------")
    # Comparação com Ibovespa
    if carteira_roi > rendimento_ibovespa:
        print("A carteira ROI superou o Ibovespa! Bom investimento!")
    else:
        print("A carteira ROI ficou abaixo do Ibovespa. É hora de reavaliar.")
        
    if carteira_mf > rendimento_ibovespa:
        print("A carteira da Magic Formula superou o Ibovespa! Estratégia eficaz!")
    else:
        print("A carteira da Magic Formula ficou abaixo do Ibovespa. É hora de reavaliar.")

if __name__ == "__main__":
    main()
