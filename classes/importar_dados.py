import pandas as pd

class DataImporter:
    def import_data(self, filename, separator=';', decimal_separator=",", dayfirst=False):
        return pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst)