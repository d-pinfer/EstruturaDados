class Pedido:
    def __init__(self, id, descricao, prioridade):
        self.id = id
        self.descricao = descricao
        self.prioridade = prioridade

class Heap:
    def __init__(self):
        self.dados = [None] * 5
        self.tamanho = 0
        self.capacidade = 5

def inicializar_heap():
    return Heap()

def inserir(heap, pedido):

    if heap.tamanho == heap.capacidade:
        heap.capacidade *= 2
        heap.dados += [None] * heap.tamanho

    i = heap.tamanho
    heap.dados[i] = pedido
    heap.tamanho += 1

    while i > 0:
        pai = (i - 1) // 2

        if heap.dados[i].prioridade > heap.dados[pai].prioridade:
            heap.dados[i], heap.dados[pai] = heap.dados[pai], heap.dados[i]
            i = pai
        else:
            break

def max_heapfy(heap, i):
    esq = 2 * i + 1
    dir = 2 * i + 2
    maior = i

    if esq < heap.tamanho and heap.dados[esq].prioridade > heap.dados[maior].prioridade:
        maior = esq

    if dir < heap.tamanho and heap.dados[dir].prioridade > heap.dados[maior].prioridade:
        maior = dir

    if maior != i:
        heap.dados[i], heap.dados[maior] = heap.dados[maior], heap.dados[i]
        max_heapfy(heap, maior)

def remover(heap):
    if heap.tamanho == 0:
        return None

    pedido = heap.dados[0]

    heap.dados[0] = heap.dados[heap.tamanho - 1]
    heap.tamanho -= 1

    if heap.tamanho > 0:
        max_heapfy(heap, 0)

    return pedido

def construir(heap):
    for i in range(heap.tamanho // 2 - 1, -1, -1):
        max_heapfy(heap, i)

def print_heap(heap):
    if heap.tamanho == 0:
        print("Nenhum pedido.")
        return

    for i in range(heap.tamanho):
        p = heap.dados[i]
        print(f"ID: {p.id} | {p.descricao} | Prioridade: {p.prioridade}")

heap = inicializar_heap()

while True:

    print("\n===== SISTEMA DE PEDIDOS =====")
    print("1 - Cadastrar pedido")
    print("2 - Atender pedido")
    print("3 - Exibir pedidos")
    print("4 - Exibir quantidade de pedidos")
    print("5 - Sair")

    opcao = int(input("Escolha: "))

    match opcao:

        case 1:
            id = int(input("ID: "))
            descricao = input("Descricao: ")
            prioridade = int(input("Prioridade: "))

            inserir(heap, Pedido(id, descricao, prioridade))

        case 2:
            pedido = remover(heap)

            if pedido == None:
                print("Nenhum pedido.")
            else:
                print("\nPedido atendido:")
                print(f"ID: {pedido.id}")
                print(f"Descricao: {pedido.descricao}")
                print(f"Prioridade: {pedido.prioridade}")

        case 3:
            print_heap(heap)

        case 4:
            print("Quantidade:", heap.tamanho)

        case 5:
            break

        case _:
            print("Opcao invalida.")
