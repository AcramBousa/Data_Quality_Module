import pandas as pd
import matplotlib.pyplot as plt
from os import path

class DataPlotter:

    def plot_data(self, dataframe, name = ''):
        dataframe.reset_index(inplace=True)
        dataframe.set_index(['start_time'], drop=True, inplace=True)

        if name == '':
            name = dataframe["PODID"].iloc[0]

        self.dataframe = dataframe["ActiveEnergy"]

        self.dataframe = pd.DataFrame(self.dataframe)
        self.dataframe.plot(title=name, xlabel="TIME", ylabel="ACTIVE ENERGY")

        plt.savefig(path.join('PELL_Plots/', f'{name}_Plot.png'))