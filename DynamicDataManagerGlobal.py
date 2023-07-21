import glob
import json

import pandas as pd


class DynamicDataManagerGlobal:

    #nome = 3

    #funzione per estrarre un dataframe da tutta la cartella PELL_Data
    def load_jsons(self, path = 'Genova', podid = None):

        # Ottieni la lista di tutti i file JSON nella cartella corrente
        json_files = glob.glob(f"PELL_Data/{path}/*.json")

        # Crea una lista vuota per i dizionari dei dati di ogni file
        data_list = []

        # Loop sui file JSON
        for file in json_files:
            # Carica il file JSON
            with open(file) as json_file:
                data = json.load(json_file)

            # Estrai i dati necessari dal JSON
            line_data = data['UrbanDataset']['values']['line']

            # Loop su tutti gli oggetti "line" all'interno di line_data
            for line_item in line_data:
                # Estrai le proprietà e i valori di ogni oggetto "line" e crea un dizionario
                line_dict = {
                    'start_ts': line_item['period']['start_ts']
                }

                # Aggiungi tutte le proprietà presenti in line_item['property'] al dizionario
                for prop in line_item['property']:
                    try:
                        line_dict[prop['name']] = float(prop['val'])
                    except ValueError:
                        line_dict[prop['name']] = prop['val']

                # Aggiungi il dizionario alla lista dei dati
                data_list.append(line_dict)

        # Crea il dataframe
        df = pd.DataFrame(data_list)

        df.rename(columns={'TotalActiveEnergy': 'ActiveEnergy'}, inplace=True)
        df.rename(columns={'start_ts': 'start_time'}, inplace=True)

        # Selezione sulla base del PODID specificato
        if podid:
            df = df[df['PODID'] == podid]

        # Imposta start_ts come indice del dataframe (facoltativo)
        df.set_index(['start_time'], drop=True, inplace=True)

        # Stampa il dataframe
        #print(df)

        return df