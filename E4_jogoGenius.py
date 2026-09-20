import random

class No:
    def __init__(self, cor):
        self.cor = cor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

def inicializar_fila():
    return Fila()

def enfileirar(fila, cor):
    novo = No(cor)

    if fila.inicio == None:
        fila.inicio = novo
        fila.fim = novo
    else:
        fila.fim.proximo = novo
        fila.fim = novo

    fila.quantidade += 1

def desenfileirar(fila):
    if fila.inicio == None:
        return None

    cor = fila.inicio.cor
    fila.inicio = fila.inicio.proximo
    fila.quantidade -= 1

    if fila.inicio == None:
        fila.fim = None

    return cor

def frente(fila):
    if fila.inicio == None:
        return None

    return fila.inicio.cor

def imprimir(fila):
    atual = fila.inicio

    while atual != None:
        print(atual.cor, end=" ")

        if atual.proximo != None:
            print("->", end=" ")

        atual = atual.proximo

    print()

def nova_partida():
    return inicializar_fila()

def adicionar_cor(fila):
    numero = random.randint(1, 4)

    if numero == 1:
        cor = "VERDE"
    elif numero == 2:
        cor = "VERMELHO"
    elif numero == 3:
        cor = "AZUL"
    else:
        cor = "AMARELO"

    enfileirar(fila, cor)

def conferir(fila):
    atual = fila.inicio

    while atual != None:

        resposta = input("Cor: ").upper()

        if resposta != atual.cor:
            return False

        atual = atual.proximo

    return True

fila = nova_partida()
pontuacao = 0
jogando = False

while True:

    print("\n================================")
    print("          JOGO GENIUS")
    print("================================")
    print(f"Pontuacao: {pontuacao}")

    print("\n--------- MENU ---------")
    print("1 - Iniciar / Continuar")
    print("2 - Reiniciar partida")
    print("0 - Sair")
    print("------------------------")

    opcao = int(input("Escolha uma opcao: "))

    match opcao:
        
        case 0:
            print("\nJogo encerrado!")
            break

        case 1:

            jogando = True

            while jogando:

                adicionar_cor(fila)

                print("\n================================")
                print(f"           RODADA {fila.quantidade}")
                print("================================")

                print("\nMemorize a sequencia:")
                imprimir(fila)

                print("\nRepita a sequencia:")

                if conferir(fila):

                    pontuacao += 1

                    print("\nVoce acertou!")
                    print(f"Pontuacao: {pontuacao}")

                    continuar = input(
                        "\nPressione ENTER para continuar ou 0 para voltar ao menu: "
                    )

                    if continuar == "0":
                        jogando = False

                else:

                    print("\n********************************")
                    print("           VOCE ERROU!")
                    print("********************************")
                    print(f"Pontuacao final: {pontuacao}")
                    print("********************************")

                    jogando = False

        case 2:

            fila = nova_partida()
            pontuacao = 0

            print("\nPartida reiniciada!")


        case _:
            print("\n[ERRO] Opcao invalida!")
