import pandas as pd
import matplotlib.pyplot as plt

class AnalisarFragmentacao:
    def __init__(self, BASE_FOLDER: str = './data_logs/logs/fragmentation.csv', MINIMUM: int = 4) -> None:
        self.BASE_FOLDER = BASE_FOLDER
        self.MINIMUM = MINIMUM

    def analyze_data(self):
        df = pd.read_csv(self.BASE_FOLDER, delimiter=';')
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.set_index('datetime')
        df['time_passed'] = (df.index - df.index[0]).total_seconds() / 3600
        df = df.set_index('time_passed')
        df_filtered = df[df['process_occurrences'] >= self.MINIMUM]
        df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')
        ax = df_pivot.plot(ylabel='Process occurrences', xlabel='Time(H)')
        return ax

    def save_plot(self, ax, filename):
        fig = ax.get_figure()
        fig.savefig(filename)