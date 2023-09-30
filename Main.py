import re

class Grafo:
    def __init__(self, lista):
        self.lista = lista

    def get_transicoes(self, v):
        return self.lista[v]

with open("MT-deterministica.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("strings.txt", "r") as arquivo:
    strings = arquivo.readlines()


def simula_MT_deterministica(linhas_tratadas, strings_tratadas, estado_final, MT):
    for i in strings_tratadas:
        palavra = list(i)
        palavra.append('_')
        ponteiro = 0
        estado_atual = linhas_tratadas[len(linhas_tratadas)-3][0]
        while(True):
            rejeita = True
            for transicao in MT.get_transicoes(estado_atual):
                if(transicao[0] == palavra[ponteiro]):
                    rejeita = False
                    estado_atual = transicao[1]
                    palavra[ponteiro] = transicao[2]
                    if(transicao[3] == 'L'):
                        ponteiro-=1
                    else:
                        ponteiro+=1
                    break
            if(estado_atual==estado_final):
                print("Palavra " + i + " aceita")
                break
            elif(rejeita):
                print("Palavra " + i + " rejeitada")
                break

    
linhas_tratadas = []
strings_tratadas = []

for linha in linhas:
    linhas_tratadas.append(re.split('[,;]', linha.strip()))

for palavra in strings:
    strings_tratadas.append(palavra.split()[0])

dicio = {}
estado_final = linhas_tratadas[len(linhas_tratadas)-2][0]


for i in range(3,len(linhas_tratadas)-3):
    estado, transicao = linhas_tratadas[i][0], tuple(linhas_tratadas[i][1:])
    if(estado in dicio):  
        dicio[estado].append(transicao)
    else:
        dicio[estado] = [transicao]

MT = Grafo(dicio)

simula_MT_deterministica(linhas_tratadas, strings_tratadas, estado_final, MT)


