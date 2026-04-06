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
        partes = 17
        
    bala = partes + 10
    return ponto, inimigos, partes, bala, nivel, jogador

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

def acao():
    xEntrada = input("Indicar a posição x - horizontal: ")
    yEntrada = input("Indicar a posição y - vertical: ")
    if str(xEntrada).isdigit() == True and str(yEntrada).isdigit() == True:
        temp = 0
        try:
            if jogador[int(yEntrada)-1][int(xEntrada)-1] != inimigos[int(yEntrada)-1][int(xEntrada)-1]:
                temp = 1
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
        except IndexError:
            renderizar()
            print("Erro ao localizar")
        return temp
    else:
        temp = "False"
        return temp

estadoDeFuncionamento = "menu"
def menu():
    os.system("cls")
    print("A Batalha naval.")
    print("")
    print("1. jogar")
    print("2. Sair")
    tecla = input("Digite o número para executar uma ação: ")
    if tecla == "1":
        estadoDeFuncionamento = "game_loading"
    else:
        estadoDeFuncionamento = "break"
    return estadoDeFuncionamento

nome = input("Digite o nome, apelido ou nome fictício de jogador: ")

while True:
    if estadoDeFuncionamento == "menu":
        estadoDeFuncionamento = menu()
    elif estadoDeFuncionamento == "game_loading":
        carregado = iniciar()
        pontos = carregado[0]
        inimigos = carregado[1]
        partes = carregado[2]
        bala = carregado[3]
        nivel = carregado[4]
        jogador = carregado[5]
        renderizar()
        estadoDeFuncionamento = "game"
    elif estadoDeFuncionamento == "game":
        print(f"Pontos {ponto} | Munição {bala}")
        temp2 = acao()
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
                    estadoDeFuncionamento = "menu"
        if str(temp2) != "False":
            ponto = ponto + int(temp2)
            if ponto == partes:
                print(f"O Jogador {nome} ganhou. | Pontos {pontos} | Pontos acumulados {pontos_salvos}")
                pontos_salvos += pontos
                input("Precione para ir ao proxima nível aleatório")
                estadoDeFuncionamento = "game_loading"
        else:
            estadoDeFuncionamento = "menu"
    else:
        break