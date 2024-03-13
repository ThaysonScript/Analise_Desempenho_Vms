from utils.tags_monitoramento import MONITORING_FILES, YLABELS
from classes.plotar_grafico import PlotarGrafico
from classes.plotar_dado import PlotarDado
from classes.analisar_fragmentacao import AnalisarFragmentacao

class Main:
    def __init__(self, analisar_dados: object, plotar_dados: object, analisar_fragmentacao: object) -> None:
        self.analisar_dados = analisar_dados
        self.plotar_dados = plotar_dados
        self.analisar_fragmentacao = analisar_fragmentacao
        
    def fragmentacao(self):
        ax = self.analisar_fragmentacao.set_analisar_dados_fragmentados()
        self.analisar_fragmentacao.set_salvar_plots_fragmentacao(ax, './images_plot/fragmentation.png')
        
    def passar_arquivos(self):
        for title, filename in MONITORING_FILES.items():
            self.analisar_dados.set_plotar(filename=f"./data_logs/logs/{filename}", title=title, ylabel=YLABELS[title], dayfirst=True)
             
             
if __name__ == "__main__":
    plotar_dados: object = PlotarDado()
    analisar_dados = PlotarGrafico(plotar_dados)
    analisar_fragmentacao: object = AnalisarFragmentacao()
    
    novo_objeto: object = Main(analisar_dados=analisar_dados, plotar_dados=plotar_dados, analisar_fragmentacao=analisar_fragmentacao)
    
    novo_objeto.fragmentacao()
    novo_objeto.passar_arquivos()