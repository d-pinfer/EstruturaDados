import math

def inicializar_array():
    return []

def inserir(array, valor):
    array.append(valor)

def imprimir(array):
    print(array)

def buscar(array, valor):
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return -1

def remover(array, valor):
    if valor in array:
        array.remove(valor)


def multiplicar_escalar(array, escalar):
    resultado = []

    for valor in array:
        resultado.append(valor * escalar)

    return resultado


def somar(a, b):
    if len(a) != len(b):
        return None

    resultado = []

    for i in range(len(a)):
        resultado.append(a[i] + b[i])

    return resultado


def produto_escalar(a, b):
    if len(a) != len(b):
        return None

    resultado = 0

    for i in range(len(a)):
        resultado += a[i] * b[i]

    return resultado


def norma(array):
    soma = 0

    for valor in array:
        soma += valor * valor

    return math.sqrt(soma)


def similaridade_cosseno(a, b):
    if len(a) != len(b):
        return None

    norma_a = norma(a)
    norma_b = norma(b)

    if norma_a == 0 or norma_b == 0:
        return None

    return produto_escalar(a, b) / (norma_a * norma_b)


# PROGRAMA

tamanho = int(input("Tamanho dos vetores: "))

a = inicializar_array()
b = inicializar_array()

print("Digite o vetor A:")

for i in range(tamanho):
    valor = float(input())
    inserir(a, valor)

print("Digite o vetor B:")

for i in range(tamanho):
    valor = float(input())
    inserir(b, valor)


print(f"\nVetor A: {a}")

print(f"Vetor B: {b}")

escalar = float(input("\22nDigite um escalar: "))

print(f"Multiplicacao por escalar:{multiplicar_escalar(a, escalar)}")

print(f"Soma: {somar(a, b)}")

print(f"Produto escalar: {produto_escalar(a, b)}")

print(f" Norma de A: {norma(a):.4f}")


similaridade = similaridade_cosseno(a, b)

if similaridade == None:
    print("Operacao invalida")
else:
    print(f"Similaridade: {similaridade:.4f}")
