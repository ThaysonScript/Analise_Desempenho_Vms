from ler_csv import ler_csv
from revisado.fragmentacao.configurar_index_data_frame import configurar_index_data_frame
from revisado.fragmentacao.fazer_plotagem import fazer_plotagem
from revisado.fragmentacao.filtrar_data_frame import filtrar_data_frame
from revisado.fragmentacao.pivotar_data_frame import pivotar_data_frame


def fragmentacao_start():
    caminho_arquivo = '../../data_logs/logs_vbox/logs_com_disco_1gb/fragmentation.csv'
    novo_data_frame = ler_csv(caminho_arquivo)

    novo_data_frame = configurar_index_data_frame(novo_data_frame)

    novo_data_frame = filtrar_data_frame(novo_data_frame)

    data_frame_pivotado = pivotar_data_frame(novo_data_frame)

    data_frame_pivotado = fazer_plotagem(data_frame_pivotado)


if __name__ == '__main__':
    fragmentacao_start()
