import pandas as pd

class ImportarDado:
    def __init__(self) -> None:
        pass
        
    def __importar_dados(self, filename, separator=';', decimal_separator=",", dayfirst=False):
        return pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst)
    
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_importar_dados(self, filename, separator=';', decimal_separator=",", dayfirst=False):
        self.__importar_dados(filename=filename, separator=separator, decimal_separator=decimal_separator, dayfirst=dayfirst)