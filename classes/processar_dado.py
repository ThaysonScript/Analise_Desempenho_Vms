import pandas as pd

class ProcessarDado:
    def __init__(self) -> None:
        pass
    
    def __processar_dados(self, df, datetime_col='date_time', division=1, cols_to_divide=[]):
        # df['seconds'] = (df[datetime_col] - df[datetime_col][0]).dt.total_seconds() / 3600
        # df = df.set_index('seconds')
        #
        # cols_to_divide = cols_to_divide if cols_to_divide else df.columns
        # df[cols_to_divide] = df[cols_to_divide].div(division)

        # df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst,
        #                  parse_dates=[datetime]).rename(columns={datetime: 'seconds'})

        # df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
        # df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))

        # cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
        # df[cols_to_divide] = df[cols_to_divide].div(division)
        
        return df
    
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_processar_dados(self, df, datetime_col='date_time', division=1, cols_to_divide=[]):
        self.__processar_dados(df=df, datetime_col=datetime_col, division=division, cols_to_divide=cols_to_divide)