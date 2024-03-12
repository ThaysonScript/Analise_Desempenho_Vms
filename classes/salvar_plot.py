class SalvarPlot:
    def __init__(self) -> None:
        pass
    
    def __salvar_plot(self, fig, filename):
        fig.savefig(filename)
        
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_salvar_plot(self, fig, filename):
        self.__salvar_plot(fig=fig, filename=filename)