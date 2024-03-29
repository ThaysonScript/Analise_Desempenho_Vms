import pandas as pd


def configurar_index_data_frame(data_frame):
    data_frame_index_configurado = data_frame

    # Convert the datetime column to a datetime object
    data_frame_index_configurado['datetime'] = pd.to_datetime(data_frame_index_configurado['datetime'])

    # Set the index to the datetime column
    data_frame_index_configurado = data_frame_index_configurado.set_index('datetime')

    data_frame_index_configurado['time_passed'] = (data_frame_index_configurado.index -
                                                   data_frame_index_configurado.index[0]).total_seconds() / 3600

    # Resetting the index to use 'time_passed' as index
    data_frame_index_configurado = data_frame_index_configurado.set_index('time_passed')

    return data_frame_index_configurado
