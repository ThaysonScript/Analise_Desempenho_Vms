import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from time import sleep

class PlotarGrafico:
    def __init__(self, plotado):
        self.plotado = plotado

    def __plotar(self, filename, ylabel, datetime="date_time", title=None, separator=';', decimal_separator=",", dayfirst=False, division=1, includeColYlabel=False, cols_to_divide=[]):
        df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst, parse_dates=[datetime]).rename(columns={datetime: 'seconds'})

        df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
        df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))

        cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
        df[cols_to_divide] = df[cols_to_divide].div(division)


        for col in df.columns:
            col_mix = col + " " + ylabel if type(ylabel) is str and includeColYlabel else ylabel

            df[col] = df[col].fillna(0)

            x = df.index.to_numpy().reshape((-1, 1))
            y = df[col].to_numpy().reshape((-1, 1))
            
            model = LinearRegression()
            model.fit(x, y)

            Y_pred = model.predict(x)
            
            ax = df.plot(
                y=col,
                legend=0,
                xlabel='Time(h)',
                ylabel=col_mix if type(ylabel) is str else ylabel[col] if type(ylabel) is dict and col in ylabel else col,
                title=title if type(title) is str else title[col] if type(title) is dict and col in title else col,
                figsize=(10,5),
                style='k',
            )      
            
            ax.plot(x, Y_pred, color='red')
            
            plt.show()
            
            fig = ax.get_figure()
            fig.savefig(f'./images_plot/{title}-{col}.png')
            
            sleep(1)
            
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
    
    def set_plotar(self, filename, title=None, ylabel=None, dayfirst=False, division=1, includeColYlabel=False, cols_to_divide=[]):
        self.__plotar(filename=filename, title=title, ylabel=ylabel, dayfirst=dayfirst, division=division, includeColYlabel=includeColYlabel, cols_to_divide=cols_to_divide)
        