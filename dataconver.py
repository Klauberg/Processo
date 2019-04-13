import datetime
class Converte:

    def __init__(self):
        pass
    #Separa a data para melhor modificações
    def converte_data(self,data):

        hora=data[0:2]
        minuto=data[3:5]
        segundo=data[6:8]
        data=[hora,minuto,segundo]
        return data

    def converte_segundos(self):
        # Pega Tempo atual
        agora = (datetime.datetime.now()).strftime("%H:%M:%S")

        # Calcula os segundos
        data = ((int(agora[0:2]) * 3600) + (int(agora[3:5]) * 60) + (int(agora[6:8])))

        return data