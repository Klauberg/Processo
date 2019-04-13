from dataconver import *

class Calculo:
    def calcula_atividade(self):
        # Cria obj para o calculo dos segundos atuais
        converte = Converte()
        agora = converte.converte_segundos()

        #Cria vetor onde processos ativos iram guardar
        processos=[]
        arquivo = open("processo.txt", "r")
        for linha in arquivo:
            atividade = linha.split('-')
            #Confere o tempo dos processos
            total = int(atividade[0]) - agora
            #Salva os processos que ainda tem tempo para o processamento
            if total>0:
                processos.append(str(atividade[0])+"-"+str(atividade[1])+"-"+str(atividade[2])+"-"+str(atividade[3]))

        #Reseta pagina dos processos
        arquivo = open("processo.txt", "w")
        arquivo.write("")

        #Rescreve os processos no txt, para o salvamento dos dados
        for i in processos:
            arquivo_escreve = open("processo.txt", "a")
            arquivo_escreve.write(i)

