import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, importer, processor, plotter, line_adder, plot_saver):
        self.importer = importer
        self.processor = processor
        self.plotter = plotter
        self.line_adder = line_adder
        self.plot_saver = plot_saver

    def plot(self, filename, title=None, ylabel=None, dayfirst=False, division=1, includeColYlabel=False, cols_to_divide=[]):
        df = self.importer.import_data(filename, dayfirst=dayfirst)
        df = self.processor.process_data(df, division=division, cols_to_divide=cols_to_divide)

        for col in df.columns:
            col_ylabel = col + " " + ylabel if includeColYlabel else ylabel
            df[col].fillna(0, inplace=True)

            x = df.index.to_numpy().reshape((-1, 1))
            y = df[col].to_numpy().reshape((-1, 1))

            ax = self.plotter.plot_data(df[[col]], title=title[col] if isinstance(title, dict) and col in title else title, ylabel=col_ylabel)
            ax = self.line_adder.add_regression_line(ax, x, y)
            plt.show()
            self.plot_saver.save_plot(ax.get_figure(), f'./plot_images/{title}-{col}.png')