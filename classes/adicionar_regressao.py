from sklearn.linear_model import LinearRegression

class AdicionarRegressao:
    def __init__(self) -> None:
        pass
        
    def __adicionar_linha_regressao(self, ax, x, y):
        modelo = LinearRegression()
        modelo.fit(x, y)
        Y_pred = modelo.predict(x)
        ax.plot(x, Y_pred, color='red')
        return ax
    
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_adicionar_linha_regressao(self, ax, x, y):
        self.__adicionar_linha_regressao(ax=ax, x=x, y=y)