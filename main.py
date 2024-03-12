from utils.tags_monitoramento import MONITORING_FILES, YLABELS
from classes.plotar_grafico import PlotarGrafico
from classes.importar_dado import ImportarDado
from classes.processar_dado import ProcessarDado
from classes.plotar_dado import PlotarDado
from classes.adicionar_regressao import AdicionarRegressao
from classes.salvar_plot import SalvarPlot
from classes.analisar_fragmentacao import AnalisarFragmentacao

class Main:
    def __init__(self, analisar_dados: object, importar_dados: object, processar_dados: object, plotar_dados: object,
                adicionar_linha_regressao: object, salvar_plots: object, analisar_fragmentacao: object) -> None:
        self.analisar_dados = analisar_dados
        self.importar_dados = importar_dados
        self.processar_dados = processar_dados
        self.plotar_dados = plotar_dados
        self.adicionar_linha_regressao = adicionar_linha_regressao
        self.salvar_plots = salvar_plots
        self.analisar_fragmentacao = analisar_fragmentacao
        
    def fragmentacao(self):
        ax = self.analisar_fragmentacao.set_analisar_dados_fragmentados()
        self.analisar_fragmentacao.set_salvar_plots_fragmentacao(ax, './images_plot/fragmentation.png')
             
if __name__ == "__main__":
    # analisar_dados: object = PlotarGrafico()
    importar_dados: object = ImportarDado()
    processar_dados: object = ProcessarDado()
    plotar_dados: object = PlotarDado()
    adicionar_linha_regressao: object = AdicionarRegressao()
    salvar_plots: object = SalvarPlot()
    analisar_fragmentacao: object = AnalisarFragmentacao()
    
    analisar_dados = PlotarGrafico(importar_dados, processar_dados, plotar_dados, adicionar_linha_regressao, salvar_plots)
    
    novo_objeto = Main(
        analisar_dados=analisar_dados, importar_dados=importar_dados, processar_dados=processar_dados, 
        plotar_dados=plotar_dados, adicionar_linha_regressao=adicionar_linha_regressao, salvar_plots=salvar_plots,
        analisar_fragmentacao=analisar_fragmentacao
    )
    
    novo_objeto.fragmentacao()

    for title, filename in MONITORING_FILES.items():
        analisar_dados.set_plotar(filename=f"./data_logs/logs/{filename}", title=title, ylabel=YLABELS[title], dayfirst=True)