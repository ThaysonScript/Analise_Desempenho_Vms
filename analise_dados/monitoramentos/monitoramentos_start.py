from carregar_data_frame import carregar_data_frame
from configurar_index_data_frame import configurar_index_data_frame
from fazer_plot_and_regress import fazer_plot_regressao
from formatar_tipo_coluna_data_frame import formatar_tipo_coluna_data_frame
from caminho_logs import arquivos

def monitoramentos_start():
    for chave, valor in arquivos.items():        
        print(f"chave: {chave}\nvalor: {valor}")

        # novo_data_frame = carregar_data_frame(caminho_novo_data_frame)

        # novo_data_frame = configurar_index_data_frame(novo_data_frame)

        # novo_data_frame = formatar_tipo_coluna_data_frame(novo_data_frame)

        # plotagem_and_regress = fazer_plot_regressao(novo_data_frame)
    
if __name__ == "__main__":
    monitoramentos_start()