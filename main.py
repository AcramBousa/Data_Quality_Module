import pandas as pd

from DynamicDataManager import DynamicDataManager
from DynamicDataManagerGlobal import DynamicDataManagerGlobal
from DataPlotter import DataPlotter
from Metriche import Metriche
from FileConverter import FileConverter


def main():

    path = 'Genova'
    podid = None
    #data_mgr = DynamicDataManager()
    #Modulo per leggere tutti i dati contenuti nei file json della cartella specificata in path;
    # per selezionare dati di uno specifico podid modificare la variabile 'podid' con il contenuto del podid da selezionare
    data_mgr_glb = DynamicDataManagerGlobal()
    df = data_mgr_glb.load_jsons(path, podid)

    #Modulo per Converire dataframe a CSV e viceversa
    file_converter = FileConverter()

    #Funzione che salva dataframe in un CSV, nella cartella PELL_CSV
    # aggiungere il parametro nome_file salverà il csv con quel nome, altrimenti userà il primo PODID presente 
    file_name = 'provaGenova'
    file_converter.df_to_csv(df,file_name)

    #Funzione che legge il csv specificato in 'csv_path'
    csv_path= 'PELL_CSV/provaGenova.csv'
    df = file_converter.csv_to_df(csv_path)

    #Modulo per salvare il grafico dell'andamento del consumo, consiglio di selezionare un podid specifico da mostrare
    data_plt = DataPlotter()
    plot_name = 'provaGenova'
    data_plt.plot_data(df, plot_name)


    print(df)

    # show_result stampa tutti i valori senza limiti
    #show_result(df)



def show_result(filtered_df):
    pd.set_option('display.max_rows', 90000)
    print(filtered_df.head(18000))

if __name__ == "__main__":
    main()