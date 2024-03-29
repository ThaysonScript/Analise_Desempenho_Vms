import pandas as pd

def configurar_index_data_frame(data_frame):  
  data_frame['date_time'] = pd.to_datetime(data_frame['date_time'], format='%d-%m-%Y-%H:%M:%S')
  data_frame_formatado_index = data_frame.set_index(data_frame['date_time'])

  data_frame_formatado_index['tempo_passado'] = data_frame_formatado_index['date_time'].dt.strftime('%H:%M:%S')
  data_frame_formatado_index['tempo_passado'] = abs(data_frame_formatado_index.index - data_frame_formatado_index.index[0]).total_seconds() / 3600

  data_frame_formatado_index = data_frame_formatado_index.set_index('tempo_passado')

  return data_frame_formatado_index