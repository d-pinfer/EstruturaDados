TAMANHO = 7

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Hash:
    def __init__(self):
        self.tabela = [None] * TAMANHO
        self.quantidade = 0

def funcao_hash(valor):
    return valor % TAMANHO

def inserir(hash, valor):
    posicao = funcao_hash(valor)
    novo = No(valor)

    if hash.tabela[posicao] == None:
        hash.tabela[posicao] = novo
    else:
        atual = hash.tabela[posicao]

        while atual.proximo != None:
            atual = atual.proximo

        atual.proximo = novo

    hash.quantidade += 1

def buscar(hash, valor):
    posicao = funcao_hash(valor)
    atual = hash.tabela[posicao]

    while atual != None:
        if atual.valor == valor:
            return True

        atual = atual.proximo

    return False

def remover(hash, valor):
    posicao = funcao_hash(valor)

    atual = hash.tabela[posicao]
    anterior = None

    while atual != None:

        if atual.valor == valor:

            if anterior == None:
                hash.tabela[posicao] = atual.proximo
            else:
                anterior.proximo = atual.proximo

            hash.quantidade -= 1
            return True

        anterior = atual
        atual = atual.proximo

    return False

def imprimir(hash):
    print("\n--- TABELA HASH ---")

    for i in range(TAMANHO):
        print(f"{i} -> ", end="")

        atual = hash.tabela[i]

        while atual != None:
            print(atual.valor, end=" ")

            atual = atual.proximo

        print()

def fator_carga(hash):
    return hash.quantidade / TAMANHO

hash = Hash()

valores = [190, 322, 172, 89, 13, 4, 769, 61, 15, 76]

for valor in valores:
    inserir(hash, valor)

imprimir(hash)

print(f"\nFator de carga: {fator_carga(hash):.2f}")

print("\nRemovendo 769...")
remover(hash, 769)
imprimir(hash)

print("\nInserindo 67...")
inserir(hash, 67)
imprimir(hash)
