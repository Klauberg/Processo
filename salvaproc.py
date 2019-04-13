from dataconver import *

class Salva:
    def __init__(self):
        pass

    def salva_processo(self,nome,tempo,tamanho):
        #Cria obj para o calculo dos segundos atuais
        converte = Converte()
        agora=converte.converte_segundos()

        # Calcula os segundos dos anteriores
        total = 0
        arquivo_leitura = open("processo.txt", "r")
        for linha in arquivo_leitura:
            #Anti-Bug(Esse bug so acontece na fase de teste devido ao remover processos e talvez fica uma linha sem querer)
            if(linha == '\n'):
                arquivo_restart =open("processo.txt", "w")
                arquivo_restart.write("")
            else:
                teste = linha.split('-')
                total = int(teste[0])-agora
        if total <0:
            total = 0

        #Escrevendo na "memoria"
        arquivo=open("processo.txt","a")
        arquivo.write(str((int(agora)+tempo+total))+"-"+nome+"-"+str(tamanho)+"-"+
                      str((datetime.datetime.now().strftime("%H:%M:%S")))+'\n')
class Leitura:

    def ler_processos(self):
        # Criando obj
        converte = Converte()
        agora = converte.converte_segundos()

        arquivo= open("processo.txt","r")
        numero = 0
        #Leitura dos processos
        for linha in arquivo:
            numero+=1
            visao = linha.split('-')
            print("\nProcesso Numero "+str(numero)+"\nNome do Processo: "+visao[1]+"\nHora inicializada: "+visao[3]+
                  "Tamanho do processo: "+visao[2]+"\nProcesso ira terminar em "+str(int(visao[0])-agora)+" Segundos\n")




