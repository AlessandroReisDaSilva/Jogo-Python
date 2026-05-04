import random
import time
import os

jogador = [
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
]

inimigos = [
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
]

inimigosTipo = [
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
]
inimigoTipo = "?"

partes = 0
ponto = 0
pontos_salvos = 0
bala = 0
nivel = 0

def iniciar():
    nivel = random.randint(1, 4)
    ponto = 0
    jogador = [
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
    ]
    inimigos = [
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
    ]
    if int(nivel) == 1:
        inimigos = [
        ["═", "╩", "═", "═", "═", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "═", "╩", "═", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "═", "╩", "═", "═", "═", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "═", "╧", "╩", "═", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "╣"],
        ["╩", "═", "▒", "░", "▒", "░", "▒", "░", "▒", "║"]
        ]
        inimigosTipo = [
        ["5", "5", "5", "5", "5", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "3", "3", "3", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "5", "5", "5", "5", "5", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "4", "4", "4", "4", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "2"],
        ["2", "2", "▒", "░", "▒", "░", "▒", "░", "▒", "2"]
        ]
        partes = 21
    elif int(nivel) == 2:
        inimigos = [
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "╩", "═", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "═", "╧", "╩", "═", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "╣"],
        ["▒", "░", "═", "╩", "═", "═", "═", "░", "▒", "║"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "═", "╧", "╩", "═", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
        ]
        inimigosTipo = [
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "2", "2", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "4", "4", "4", "4", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "2"],
        ["▒", "░", "5", "5", "5", "5", "5", "░", "▒", "2"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "4", "4", "4", "4", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
        ]
        partes = 17
    elif int(nivel) == 3:
        inimigos = [
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "╩", "═", "░", "▒", "░", "▒", "░", "▒", "╣"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "║"],
        ["║", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["╣", "▒", "░", "▒", "░", "▒", "░", "╩", "═", "▒"],
        ["║", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["║", "▒", "░", "╩", "═", "▒", "░", "▒", "░", "▒"],
        ["║", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "╩", "═", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
        ]
        inimigosTipo = [
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "2", "2", "░", "▒", "░", "▒", "░", "▒", "2"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "2"],
        ["5", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["5", "▒", "░", "▒", "░", "▒", "░", "2", "2", "▒"],
        ["5", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["5", "▒", "░", "2", "2", "▒", "░", "▒", "░", "▒"],
        ["5", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "2", "2", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
        ]
        partes = 15
    else:
        inimigos = [
        ["░", "▒", "░", "▒", "░", "▒", "╩", "═", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "═", "╩", "═", "═", "═", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "═", "╧", "╩", "═", "░", "▒", "║"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "╢"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "╣"],
        ["░", "╩", "═", "▒", "░", "▒", "░", "▒", "░", "║"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
        ]
        inimigosTipo = [
        ["░", "▒", "░", "▒", "░", "▒", "2", "2", "░", "▒"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "░", "5", "5", "5", "5", "5", "░"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒"],
        ["▒", "░", "▒", "4", "4", "4", "4", "░", "▒", "4"],
        ["░", "▒", "░", "▒", "░", "▒", "░", "▒", "░", "4"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "4"],
        ["░", "2", "2", "▒", "░", "▒", "░", "▒", "░", "4"],
        ["▒", "░", "▒", "░", "▒", "░", "▒", "░", "▒", "░"]
        ]
        partes = 17
        
    bala = partes + 10
    return ponto, inimigos, partes, bala, nivel, jogador, inimigosTipo

debug = False

def renderizar():
    os.system("cls")
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(10):
        if i == 9:
            print(f"{i+1}", end="")
        else:
            print(f"{i+1} ", end="")
        for j in range(10):
            print(f" {jogador[i][j]} ", end="")
        print("\n")
    if debug == True:
        print("\n")
        for i in range(10):
            if i == 9:
                print(f"{i+1}", end="")
            else:
                print(f"{i+1}  ", end="")
            for j in range(10):
                print(f" {inimigos[i][j]}{inimigosTipo[i][j]} ", end="")
            print("\n")

def acao():
    xEntrada = input("Indicar a posição x - horizontal: ")
    yEntrada = input("Indicar a posição y - vertical: ")
    if str(xEntrada).isdigit() == True and str(yEntrada).isdigit() == True and str(xEntrada).isspace() == False and str(yEntrada).isspace() == False:
        temp = 0
        inimigoTipo = "?"
        try:
            if jogador[int(yEntrada)-1][int(xEntrada)-1] != inimigos[int(yEntrada)-1][int(xEntrada)-1] and jogador[int(yEntrada)-1][int(xEntrada)-1] != "x":
                temp = 1
                if inimigosTipo[int(yEntrada)-1][int(xEntrada)-1] == "5":
                    inimigoTipo = "═╩═══ 5"
                elif inimigosTipo[int(yEntrada)-1][int(xEntrada)-1] == "4":
                    inimigoTipo = "═╧╩═ 4"
                elif inimigosTipo[int(yEntrada)-1][int(xEntrada)-1] == "3":
                    inimigoTipo = "═╩═ 3"
                elif inimigosTipo[int(yEntrada)-1][int(xEntrada)-1] == "2":
                    inimigoTipo = "╩═ 2"
                else:
                    inimigoTipo = "?"
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "◦"
                renderizar()
                time.sleep(0.1)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "●"
                renderizar()
                time.sleep(0.1)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "○"
                renderizar()
                time.sleep(0.1)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "◌"
                renderizar()
                time.sleep(0.1)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = inimigos[int(yEntrada)-1][int(xEntrada)-1]
                renderizar()
            elif jogador[int(yEntrada)-1][int(xEntrada)-1] == "░" or jogador[int(yEntrada)-1][int(xEntrada)-1] == "▒":
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "▪"
                renderizar()
                time.sleep(0.1)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "■"
                renderizar()
                time.sleep(0.1)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "□"
                renderizar()
                time.sleep(0.1)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "x"
                renderizar()
                inimigoTipo = "?"
            elif jogador[int(yEntrada)-1][int(xEntrada)-1] == "x":
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "█"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "x"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "█"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "x"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "█"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "x"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "█"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "x"
                renderizar()
            else:
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "█"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = inimigos[int(yEntrada)-1][int(xEntrada)-1]
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "█"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = inimigos[int(yEntrada)-1][int(xEntrada)-1]
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = "█"
                renderizar()
                time.sleep(0.5)
                jogador[int(yEntrada)-1][int(xEntrada)-1] = inimigos[int(yEntrada)-1][int(xEntrada)-1]
                renderizar()
        except IndexError:
            renderizar()
            print("Erro ao localizar")
        return temp, inimigoTipo
    else:
        temp = "False"
        inimigoTipo = "?"
        return temp, inimigoTipo

estadoDeFuncionamento = "menu"
def menu():
    os.system("cls")
    print("A Batalha naval.")
    print("")
    print("1. jogar")
    print("2. Sair")
    tecla = input("Digite o número para executar uma ação: ")
    if tecla == "1":
        estadoDeFuncionamento = "start"
    else:
        estadoDeFuncionamento = "break"
    return estadoDeFuncionamento

nome = input("Digite o nome, apelido ou nome fictício de jogador: ")

while True:
    if estadoDeFuncionamento == "menu":
        estadoDeFuncionamento = menu()
    elif estadoDeFuncionamento == "start":
        tempo_inicial = time.time()
        estadoDeFuncionamento = "game_loading"
    elif estadoDeFuncionamento == "game_loading":
        carregado = iniciar()
        pontos = carregado[0]
        inimigos = carregado[1]
        partes = carregado[2]
        bala = carregado[3]
        nivel = carregado[4]
        jogador = carregado[5]
        inimigosTipo = carregado[6]
        renderizar()
        estadoDeFuncionamento = "game"
    elif estadoDeFuncionamento == "game":
        print(f"Pontos {ponto} | Munição {bala} | Tipo de navio: {inimigoTipo}")
        temp2 = acao()
        inimigoTipo = temp2[1]
        bala -= 1
        if bala <= 0:
                print(f"O Jogador {nome} perdeu. | Pontos {pontos} | Pontos acumulados {pontos_salvos}")
                pontos_salvos += pontos
                print("1. jogar nível aleatório")
                print("2. Sair")
                escolha = input("Escreva um número:")
                if escolha == "1":
                    estadoDeFuncionamento = "game_loading"
                else:
                    tempo_final = time.time()
                    duracao = int(tempo_final - tempo_inicial)
                    dados = []
                    if os.path.isfile("placar.txt"):
                        with open("placar.txt", "r") as arq:
                            dados = arq.readlines()

                    dados.append(f"{nome};{pontos_salvos};{duracao}\n")

                    with open("placar.txt", "a+") as arq:
                        arq.write(f"{nome};{pontos_salvos};{duracao}\n")
                    
                    print("  Nº Nome do Jogador.........: Pontos Acumulados: Tempo.:")
                    placar = sorted(dados, key=lambda x: (int(x.split(';')[1]), int(x.split(';')[2])*-1), reverse=True)
                    posicao = 0        
                    for linha in placar:
                        partes = linha.split(";")    
                        posicao += 1
                        if partes[0] == nome and int(partes[1]) == pontos and int(partes[2]) == duracao:    
                            print(f"► {posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}               {int(partes[2]):3d} seg")
                        else:
                            print(f"  {posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}               {int(partes[2]):3d} seg")
                    input("Precione Enter para sair do placar.")
                    estadoDeFuncionamento = "menu"
        if str(temp2[0]) != "False":
            ponto = ponto + int(temp2[0])
            if ponto == partes:
                print(f"O Jogador {nome} ganhou. | Pontos {pontos} | Pontos acumulados {pontos_salvos}")
                pontos_salvos += pontos
                print("1. jogar nível aleatório")
                print("2. Sair")
                escolha = input("Escreva um número:")
                if escolha == "1":
                    estadoDeFuncionamento = "game_loading"
                else:
                    tempo_final = time.time()
                    duracao = int(tempo_final - tempo_inicial)
                    dados = []
                    if os.path.isfile("placar.txt"):
                        with open("placar.txt", "r") as arq:
                            dados = arq.readlines()

                    dados.append(f"{nome};{pontos_salvos};{duracao}\n")

                    with open("placar.txt", "a+") as arq:
                        arq.write(f"{nome};{pontos_salvos};{duracao}\n")
                    
                    print("   Nº Nome do Jogador.........: Pontos Acumulados: Tempo.:")
                    placar = sorted(dados, key=lambda x: (int(x.split(';')[1]), int(x.split(';')[2])*-1), reverse=True)
                    posicao = 0        
                    for linha in placar:
                        partes = linha.split(";")    
                        posicao += 1
                        if partes[0] == nome and int(partes[1]) == pontos and int(partes[2]) == duracao:    
                            print(f"► {posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}               {int(partes[2]):3d} seg")
                        else:
                            print(f"  {posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}               {int(partes[2]):3d} seg")
                    input("Precione Enter para sair do placar.")
                    estadoDeFuncionamento = "menu"
        else:
            tempo_final = time.time()
            duracao = int(tempo_final - tempo_inicial)
            dados = []
            if os.path.isfile("placar.txt"):
                with open("placar.txt", "r") as arq:
                    dados = arq.readlines()

            dados.append(f"{nome};{pontos_salvos};{duracao}\n")

            with open("placar.txt", "a+") as arq:
                arq.write(f"{nome};{pontos_salvos};{duracao}\n")
                    
            print("   Nº Nome do Jogador.........: Pontos Acumulados: Tempo.:")
            placar = sorted(dados, key=lambda x: (int(x.split(';')[1]), int(x.split(';')[2])*-1), reverse=True)
            posicao = 0        
            for linha in placar:
                partes = linha.split(";")    
                posicao += 1
                if partes[0] == nome and int(partes[1]) == pontos and int(partes[2]) == duracao:    
                    print(f"► {posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}               {int(partes[2]):3d} seg")
                else:
                    print(f"  {posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}               {int(partes[2]):3d} seg")
            input("Precione Enter para sair do placar.")
            estadoDeFuncionamento = "menu"
    else:
        break