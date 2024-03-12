import pandas as pd

class AnalisarFragmentacao:
    def __init__(self, PASTA_LOGS: str = './data_logs/logs/fragmentation.csv', MINIMO: int = 4) -> None:
        self.PASTA_LOGS = PASTA_LOGS
        self.MINIMO = MINIMO

    def __analisar_dados_fragmentados(self):
        df = pd.read_csv(self.PASTA_LOGS, delimiter=';')
        
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.set_index('datetime')
        
        df['time_passed'] = (df.index - df.index[0]).total_seconds() / 3600
        df = df.set_index('time_passed')
        
        df_filtered = df[df['process_occurrences'] >= self.MINIMO]
        
        df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')
        ax = df_pivot.plot(ylabel='Process occurrences', xlabel='Time(H)')
        
        return ax

    def __salvar_plots_fragmentacao(self, ax, filename) -> None:
        fig = ax.get_figure()
        fig.savefig(filename)
        
    # ---------------------------------------------- GETTERS AND SETTERS ------------------------------------- #
        
    def set_analisar_dados_fragmentados(self):
        return self.__analisar_dados_fragmentados()
        
    def set_salvar_plots_fragmentacao(self, ax, filename: str) -> None:
        self.__salvar_plots_fragmentacao(ax=ax, filename=filename)