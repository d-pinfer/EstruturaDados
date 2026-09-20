class No:
    def __init__(self, disco):
        self.disco = disco
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.quantidade = 0

def inicializar_pilha():
    return Pilha()

def empilhar(pilha, disco):
    novo = No(disco)
    novo.proximo = pilha.topo
    pilha.topo = novo
    pilha.quantidade += 1

def desempilhar(pilha):
    if pilha.topo == None:
        return None

    disco = pilha.topo.disco
    pilha.topo = pilha.topo.proximo
    pilha.quantidade -= 1

    return disco

def topo(pilha):
    if pilha.topo == None:
        return None

    return pilha.topo.disco

def imprimir(pilha):
    atual = pilha.topo

    if atual == None:
        print("[ vazia ]")
        return

    print("[ ", end="")

    while atual != None:
        print(atual.disco, end=" ")
        atual = atual.proximo

    print("]")

def mostrar_torres(t1, t2, t3):
    print("\n================================")
    print("        TORRE DE HANOI")
    print("================================")

    print("Torre 1: ", end="")
    imprimir(t1)

    print("Torre 2: ", end="")
    imprimir(t2)

    print("Torre 3: ", end="")
    imprimir(t3)

    print("================================")

def nova_partida():
    t1 = inicializar_pilha()
    t2 = inicializar_pilha()
    t3 = inicializar_pilha()

    empilhar(t1, 4)
    empilhar(t1, 3)
    empilhar(t1, 2)
    empilhar(t1, 1)

    return t1, t2, t3

t1, t2, t3 = nova_partida()
movimentos = 0

while True:

    mostrar_torres(t1, t2, t3)

    print(f"\nMovimentos realizados: {movimentos}")

    print("\n--------- MENU ---------")
    print("1 - Fazer movimento")
    print("2 - Reiniciar partida")
    print("0 - Sair")
    print("------------------------")

    opcao = int(input("Escolha uma opcao: "))

    match opcao:

        case 0:
            print("\nJogo encerrado!")
            break

        case 1:
            print("\n--- NOVO MOVIMENTO ---")

            origem = int(input("Torre de origem (1, 2 ou 3): "))
            destino = int(input("Torre de destino (1, 2 ou 3): "))

            if origem == 1:
                torre_origem = t1
            elif origem == 2:
                torre_origem = t2
            elif origem == 3:
                torre_origem = t3
            else:
                print("\n[ERRO] Torre de origem invalida!")
                continue

            if destino == 1:
                torre_destino = t1
            elif destino == 2:
                torre_destino = t2
            elif destino == 3:
                torre_destino = t3
            else:
                print("\n[ERRO] Torre de destino invalida!")
                continue

            if origem == destino:
                print("\n[ERRO] Escolha torres diferentes!")

            elif topo(torre_origem) == None:
                print("\n[ERRO] A torre de origem esta vazia!")

            elif topo(torre_destino) != None and topo(torre_origem) > topo(torre_destino):
                print("\n[ERRO] Um disco maior nao pode ficar sobre um menor!")

            else:
                disco = desempilhar(torre_origem)
                empilhar(torre_destino, disco)

                movimentos += 1

                print(f"\nMovimento realizado: disco {disco}")
                print(f"Torre {origem} -> Torre {destino}")

            if t3.quantidade == 4:
                mostrar_torres(t1, t2, t3)

                print("\n********************************")
                print("          VOCE VENCEU!")
                print("********************************")
                print(f"Total de movimentos: {movimentos}")
                print("********************************")
                break

        case 2:
            t1, t2, t3 = nova_partida()
            movimentos = 0

            print("\nPartida reiniciada!")

        case _:
            print("\n[ERRO] Opcao invalida!")
