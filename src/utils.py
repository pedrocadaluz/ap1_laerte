import pandas as pd


def calcular_rendimento(df):
    """Função para calcular o rendimento percentual de uma ação."""
    if isinstance(df, list):
        # Assumindo que df é uma lista de dicionários com 'data' e 'fechamento'
        df = pd.DataFrame(df)

    df['data'] = pd.to_datetime(df['data'])
    df = df.sort_values(by='data')
    inicial = df['fechamento'].iloc[0]
    final = df['fechamento'].iloc[-1]
    rendimento = ((final - inicial) / inicial) * 100
    return rendimento