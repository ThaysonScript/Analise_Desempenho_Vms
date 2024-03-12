class ProcessarDado:
    def __init__(self) -> None:
        pass
    
    def __processar_dados(self, df, datetime_col='date_time', division=1, cols_to_divide=[]):
        df['seconds'] = (df[datetime_col] - df[datetime_col][0]).dt.total_seconds() / 3600
        df = df.set_index('seconds')
        
        cols_to_divide = cols_to_divide if cols_to_divide else df.columns
        df[cols_to_divide] = df[cols_to_divide].div(division)
        
        return df
    
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_processar_dados(self, df, datetime_col , division , cols_to_divide):
        self.__processar_dados(df=df, datetime_col=datetime_col, division=division, cols_to_divide=cols_to_divide)