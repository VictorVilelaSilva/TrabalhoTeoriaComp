import re
import copy

class Grafo:
    def __init__(self, lista):
        self.lista = lista

    def get_transicoes(self, v):
        return self.lista[v]

class Instancia_MT:
    def __init__(self, estado_atual, caminho, palavra, ponteiro):
        self.estado_atual = estado_atual
        self.caminho = caminho
        self.palavra = palavra
        self.ponteiro = ponteiro

def configura_maquina(nome_arqv, tipo):
    # Ler arquivo de configuração
    with open(nome_arqv, "r") as arquivo:
        linhas = arquivo.readlines()
    # Tratar linhas e strings
    linhas_tratadas = []
    strings_tratadas = []

    for linha in linhas:
        linhas_tratadas.append(re.split('[,;]', linha.strip()))

    for palavra in strings:
        strings_tratadas.append(palavra.split()[0])

    # Criar dicionário de estados e transições
    dicio = {}
    estado_final = linhas_tratadas[len(linhas_tratadas)-2][0]

    for i in range(3,len(linhas_tratadas)-3):
        estado, transicao = linhas_tratadas[i][0], tuple(linhas_tratadas[i][1:])
        if(estado in dicio): 
            dicio[estado].append(transicao)
        else:
            dicio[estado] = [transicao]

    # Criar grafo da máquina de Turing
    MT = Grafo(dicio)

    # Simular máquina de Turing
    if(tipo == 1):
        simula_MT_deterministica(linhas_tratadas, strings_tratadas, estado_final, MT)
    else:
        simula_MT_nao_deterministica(linhas_tratadas, strings_tratadas, estado_final, MT)
            
def simula_MT_deterministica(linhas_tratadas, strings_tratadas, estado_final, MT):
    # Simula MT determinístico.
    for i in strings_tratadas:
        # Processa cada palavra.
        palavra = list(i)
        palavra.append('_')
        ponteiro = 0
        estado_atual = linhas_tratadas[len(linhas_tratadas)-3][0]
        while(True):
            # Executa loop até aceitar ou rejeitar.
            rejeita = True
            for transicao in MT.get_transicoes(estado_atual):
                # Verifica transições possíveis.
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

def simula_MT_nao_deterministica(linhas_tratadas, strings_tratadas, estado_final, MT):
    # Simula a execução de uma Máquina de Turing não determinística.
    for i in strings_tratadas:
        # Para cada palavra na lista de palavras tratadas.
        palavra = list(i)
        palavra.append('_')
        fila_execucao = []
        maquina = Instancia_MT(linhas_tratadas[len(linhas_tratadas)-3][0], [], palavra, 0)
        fila_execucao.append(maquina)
        aceito = False
        while(len(fila_execucao)!=0):
            # Enquanto houver instâncias na fila de execução.
            instancia = fila_execucao[0]
            for transicao in MT.get_transicoes(instancia.estado_atual):
                # Para cada transição possível a partir do estado atual da instância.
                if(transicao[0] == instancia.palavra[instancia.ponteiro]):
                    # Se a transição é aplicável (o símbolo lido é igual ao símbolo da transição).
                    novo_estado = copy.deepcopy(instancia)
                    novo_estado.estado_atual = transicao[1]
                    novo_estado.palavra[novo_estado.ponteiro] = transicao[2]
                    if(transicao[3] == 'L'):
                        novo_estado.ponteiro-=1
                    else:
                        novo_estado.ponteiro+=1
                    novo_estado.caminho.append(instancia.estado_atual)
                    fila_execucao.append(novo_estado)
                    if(novo_estado.estado_atual==estado_final):
                        aceito = True
                        novo_estado.caminho.append(estado_final)
                        print("Palavra " + i + " aceita")
                        print("Caminho: " + str(novo_estado.caminho))
                        break
            fila_execucao.pop(0)
            if(aceito):
                break
        if(not aceito):
            print("Palavra " + i + " rejeitada")
                
print("Voce deseja testar para que tipo de maquina de Turing?")
escolha = input("1-Maquina de Turing Determinista / 2-Maquina de Turing Não Determinista\n")

print("Qual arquivo deseja como entrada (com extensao)?")
nome = input("")

with open(nome, "r") as arquivo:
    strings = arquivo.readlines()

if(int(escolha) == 1):
    configura_maquina('MT-deterministica.txt', 1)
else:
    configura_maquina('MT-nao-deterministica.txt', 2)



