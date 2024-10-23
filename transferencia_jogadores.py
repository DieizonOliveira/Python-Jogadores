import csv
from itertools import groupby
from operator import itemgetter

times = []

with open("top250-00-19.csv") as arq:
    linhas = csv.DictReader(arq)
    for linha in linhas:
        times.append(linha)

def titulo(texto):
    print()
    print(texto)
    print("="*40)

def top10jogadores():
    #Clubes mais compraram jogadores.
    #Cria lista de times
    time = list(set([x['Team_to'] for x in times]))

    #armazena o numero de compras feitas por cada time
    numeros = [0] * len(times)
    #percorre a lista e incrementa a lista que armazena o numero de compras de cada time
    for clube in times:

        indice = time.index(clube['Team_to'])

        numeros[indice] +=1
    #ordena a lista em ordem invera para deixar no topo os times que mais compraram
    juntos = sorted(zip(numeros, time), reverse=True)

    numeros2, times2 = zip(*juntos)

    titulo("Top 10 - Clubes que mais compraram jogadores")

    print("\nClube............................. Nº Jogadores")    

    print("-------------------------------------------------1")
    #exibe o top 10 dos times que mais compraram jogadores.
    for contador, (clube, num) in enumerate(zip(times2, numeros2), start=1):

        print(f"{contador:2d} {clube:30s} {num}")

        if contador == 10:

            break




def top10valores():
    #cria lista de clubes
    clubes = list(set([x['Team_to'] for x in times]))

    #aramazena os valores das transacoes nas compras dos jogadores
    transacoes = {clube: 0 for clube in clubes}

   #percorre os dados para trazer os valores da compra dos jogadores e converte para float.
    for transacao in times:
        clube = transacao['Team_to']
        try:
            valor = float(transacao['Transfer_fee']) 
        except ValueError:
            valor = 0  
        transacoes[clube] += valor

   #ordena de forma que fiquem no topo os clubes que tiveram as maiores transacoes
    clubes_ordenados = sorted(transacoes.items(), key=lambda x: x[1], reverse=True)

    
    print("Top 10 - Clubes com as transações de maiores valores")
    print("\nClube............................. Valores")
    print("-------------------------------------------------")
    #exibe as 10 maiores transacoes.
    for contador, (clube, valor) in enumerate(clubes_ordenados[:10], 1):
        print(f"{contador:2d} {clube:30s} {valor:.2f}")


def pesquisa_jogador():
# - Pesquisar por nome do jogador. Exibir os jogadores com o nome informado 
# (ou mensagem, caso não encontrado)
    jogador = input("Nome do jogador: ").upper()


    titulo("Historico do Jogador")
    print("Times                  Idade | Temporada")
    contador = 0  
    for i in times:
        if jogador in i['Name'].upper():
            print(f"{i['Team_to']:25s} {i['Age']} | {i['Season']}")
            contador +=1

    if contador == 0:
        print("Nome não encontrado na lista, Digite outro nome ")

def idade_media_jogadores():
# - Ler um clube. Exibir nome e idade dos jogadores comprados pelo clube e
    #  ao final, a média das idades
    nomeClube = input("Nome Completo do Clube: ").upper()


    titulo("Jogadores do Clube")
    print("Nome                  Idade | Temporada")
    contador = 0  
    idade = 0
    for i in times:
        if nomeClube in i['Team_from'].upper():
            print(f"{i['Name']:23s} {i['Age']} | {i['Season']}")
            contador +=1
            idade += int(i['Age'])

    media = idade / contador
    # print(idade)
    # print(contador)
    print(f"Média de idade: {media:.2f}")

    if contador == 0:
       print("Nome não encontrado na lista, Digite outro nome ") 

def compara_times():
    clube1 = input("Nome do primeiro clube: ").upper()
    clube2 = input("Nome do segundo clube: ").upper()

    contador1 = sum(1 for i in times if clube1 in i['Team_to'].upper())
    contador2 = sum(1 for i in times if clube2 in i['Team_to'].upper())

    titulo(f"Comparação entre {clube1} e {clube2}")
    print(f"{clube1}: {contador1} jogadores comprados")
    print(f"{clube2}: {contador2} jogadores comprados")




#--------------------------------------------------Programa Principal

while True:
    titulo("Transferências de Jogadores de Futebol")
    print("1. Top 10 - Clubes que mais compraram jogadores")
    print("2. Top 10 - Clubes com as transações de maiores valores")
    print("3. Pesquisa por nome de jogador")
    print("4. Idade média de jogadores por clube")
    print("5. Compara Times")
    print("6. Encerrar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top10jogadores()
    elif opcao == 2:
        top10valores()
    elif opcao == 3:
        pesquisa_jogador()
    elif opcao == 4:
        idade_media_jogadores()
    elif opcao == 5:
       compara_times ()
    else:
        break