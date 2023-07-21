import glob
import json

import pandas as pd


class DynamicDataManager:

    #nome = 3

    #funzione per estrarre un dataframe da tutta la cartella PELL_Data
    def load_jsons(self, path, podid):

        # Lista di tutti i file JSON nella cartella PELL_Data
        json_files = glob.glob(f"PELL_Data/{path}/*.json")

        # Crea una lista vuota per i dataframe intermedi
        dfs = []

        # Loop sui file JSON all'interno di PELL_Data
        for file in json_files:
            # Chiama funzione load_json per estrarre dataframe da un singolo JSON presente in 'file'
            df = self.load_json(file)
            # Aggiungi il dataframe alla lista dei dataframe intermedi
            dfs.append(df)

        # Combina tutti i dataframe intermedi in un unico dataframe
        combined_df = pd.concat(dfs, ignore_index=False)

        # Selezione sulla base del PODID specificato
        if podid:
            combined_df = combined_df[combined_df['PODID'] == podid]
        
        # Stampa il dataframe
        #print(df)

        return combined_df

    #Funzione per estrarre un dataframe da un singolo JSON
    def load_json(self, file):

        # Carica il file JSON
        with open(file) as json_file:
            data = json.load(json_file)

        # Estrai i dati necessari dal JSON
        line_data = data['UrbanDataset']['values']['line']

        # Crea una lista vuota per i valori di ActiveEnergy e start_ts
        start_ts_values = []
        active_energy_values = []
        podid_values = []

        # Itera su tutte le proprietà presenti nella lista "line"
        for line_item in line_data:
            # Estrai il valore di "ActiveEnergy" e "start_ts" per ogni oggetto "line"
            start_ts = line_item['period']['start_ts']
            active_energy = next(prop['val'] for prop in line_item['property'] if prop['name'] == 'TotalActiveEnergy')
            podid = next(prop['val'] for prop in line_item['property'] if prop['name'] == 'PODID')

            start_ts_values.append((start_ts))
            active_energy_values.append(float(active_energy))
            podid_values.append((podid))

        # Crea il dataframe
        df = pd.DataFrame({'start_time': start_ts_values, 'ActiveEnergy': active_energy_values, 'PODID': podid_values})

        # Cambia formato data in modo da essere più leggibile
        df['start_time'] = pd.to_datetime(df['start_time'], format='%Y-%m-%d %H:%M:%S')

        # Imposta start_ts come indice del dataframe (facoltativo)
        df.set_index(['start_time'], drop=True, inplace=True)

        # Stampa il dataframe
        #print(df)

        return df