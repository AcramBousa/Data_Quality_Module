import pandas as pd

class FileConverter:

    def df_to_csv(self, df, name = None):

        podid = df["PODID"].iloc[0]
        if name:
            df.to_csv(f'PELL_CSV/{name}.csv', sep=';')
        else:
            df.to_csv(f'PELL_CSV/{podid}.csv', sep=';')

        return 
    
    def csv_to_df(self, path):

        df = pd.read_csv(path, sep=';')

        df.set_index(['start_time'], drop=True, inplace=True)

        return df
    