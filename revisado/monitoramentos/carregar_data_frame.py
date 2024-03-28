import pandas as pd

def carregar_data_frame(arquivo_caminho):
  return pd.read_csv(arquivo_caminho, sep=';', parse_dates=['date_time'])
