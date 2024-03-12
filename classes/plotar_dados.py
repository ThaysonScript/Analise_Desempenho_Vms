class DataPlotter:
    def plot_data(self, df, title=None, ylabel=None):
        ax = df.plot(
            legend=0,
            xlabel='Time(h)',
            ylabel=ylabel,
            title=title,
            figsize=(10,5),
            style='k',
        )
        return ax