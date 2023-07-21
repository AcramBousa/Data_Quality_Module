

class Metriche:
    
    #### PER FILIPPO DA IMPLEMENTARE 

    def funzioneControllo(self, df):

        #
        #panda_DF = panda_DF[(panda_DF['start_time'] >= self.start_t) & (panda_DF['end_time'] <= self.end_t)]

        #Seleziona da df le righe con ActiveEnergy = 0
        df1 = df[(df['ActiveEnergy'] == 0)]
        #Selezione da df le righe con la data compresa tra x e y
        df2 = df[(df['start_time'] >= '2020-06-30 00:00:00') & () ]
        #Selezione da df2 la colonna Active Energy
        df2['ActiveEnergy']

        #df[]

        #output = "ci sono" + x + "errori"
        return #output
