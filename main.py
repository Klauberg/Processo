#Codigo feito por Matheus Klauberg, sem referencia.. so baseado nas aulas do Professor Patryck
#Unica coisa pesquisa sobre esse codigo foi o funcionamento do datetime no python
from salvaproc import *
from calculo import *
while True:

        escolha=input("1-Para adicionar um processo\n2-Para ver os processos ativos\n3-Sair\nEscolha: ")
        #Faz a conferencias dos processos ativos
        calculo = Calculo()
        calculo.calcula_atividade()

        #Criação de um processo
        if(escolha=="1"):
            nome = str(input ("Nome do processo:\n"))
            tempo = int(input("Digite tempo(Segundos):\n"))
            tamanho= int(input("Digite o tamanho:\n"))
            salva = Salva()
            salva.salva_processo(nome,tempo,tamanho)

        #Leitura dos processos ativos
        elif(escolha=="2"):
            leitura= Leitura()
            leitura.ler_processos()

        #Sai do programa
        elif(escolha=="3"):
            break
        else:
            print("Escolha Invalida, Tente Novamente")