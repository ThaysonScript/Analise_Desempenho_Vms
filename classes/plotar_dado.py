class PlotarDado:
    def __init__(self) -> None:
        pass
    
    def __plotar_dados(self, df, title=None, ylabel=None):
        ax = df.plot(
            legend=0,
            xlabel='Time(h)',
            ylabel=ylabel,
            title=title,
            figsize=(10,5),
            style='k',
        )
        return ax
    
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_plotar_dados(self, df, title, ylabel):
        self.__plotar_dados(df=df, title=title, ylabel=ylabel)