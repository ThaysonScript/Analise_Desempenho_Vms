from utils.tags_monitoramento import monitoring_files, ylabels
from classes.plot_graphics import DataAnalyzer
from classes.importar_dados import DataImporter
from classes.processar_dados import DataProcessor
from classes.plotar_dados import DataPlotter
from classes.adicionar_regressao import RegressionLineAdder
from classes.salvar_plots import PlotSaver
from classes.analisar_fragmentacao import AnalisarFragmentacao

class Main:
    def __init__(self) -> None:
        pass
     

if __name__ == "__main__":
    data_analyzer: object = DataAnalyzer()
    importer: object = DataImporter()
    processor: object = DataProcessor()
    plotter: object = DataPlotter()
    line_adder: object = RegressionLineAdder()
    plot_saver: object = PlotSaver()
    
    analisar_fragmentacao: object = AnalisarFragmentacao()
    
    ax = analisar_fragmentacao.analyze_data()
    analisar_fragmentacao.save_plot(ax, './images_plot/fragmentation.png')
    
    for title, filename in monitoring_files.items():
        data_analyzer.plot(filename=f"./data_logs/logs/{filename}", title=title, ylabel=ylabels[title], dayfirst=True)

    data_analyzer = DataAnalyzer(importer, processor, plotter, line_adder, plot_saver)
