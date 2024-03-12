import matplotlib.pyplot as plt

class PlotarGrafico:
    def __init__(self, importado, processado, plotado, linha_regressao_adicionada, plots_salvos):
        self.importado = importado
        self.processado = processado
        self.plotado = plotado
        self.linha_regressao_adicionada = linha_regressao_adicionada
        self.plots_salvos = plots_salvos

    def __plotar(self, filename, title=None, ylabel=None, dayfirst=False, division=1, includeColYlabel=False, cols_to_divide=[]):
        df = self.importado.set_importar_dados(filename, dayfirst=dayfirst)
        df = self.processado.set_processar_dados(df, division=division, cols_to_divide=cols_to_divide)

        for col in df.columns:
            col_ylabel = col + " " + ylabel if includeColYlabel else ylabel
            df[col].fillna(0, inplace=True)

            x = df.index.to_numpy().reshape((-1, 1))
            y = df[col].to_numpy().reshape((-1, 1))

            ax = self.plotado.plot_data(df[[col]], title=title[col] if isinstance(title, dict) and col in title else title, ylabel=col_ylabel)
            ax = self.linha_regressao_adicionada.add_regression_line(ax, x, y)
            plt.show()
            self.plots_salvos.save_plot(ax.get_figure(), f'./plot_images/{title}-{col}.png')
            
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_plotar(self, filename, title=None, ylabel=None, dayfirst=False, division=1, includeColYlabel=False, cols_to_divide=[]):
        self.__plotar(filename=filename, title=title, ylabel=ylabel, dayfirst=dayfirst, division=division, 
                      includeColYlabel=includeColYlabel, cols_to_divide=cols_to_divide)
        