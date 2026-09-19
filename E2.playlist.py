class Musica:
    def __init__(self, id, titulo, artista, album, duracao):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

class No:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class Lista:
    def __init__(self):
        self.primeiro = None
        self.quantidade = 0

def inicializar_lista():
    return Lista()

def inserir(lista, musica, posicao=None):
    novo = No(musica)

    # Lista vazia ou início
    if lista.primeiro == None or posicao == 1:
        novo.proximo = lista.primeiro
        lista.primeiro = novo

    # Final
    elif posicao == None or posicao > lista.quantidade:
        atual = lista.primeiro

        while atual.proximo != None:
            atual = atual.proximo

        atual.proximo = novo

    # Posição determinada
    else:
        atual = lista.primeiro

        for i in range(posicao - 2):
            atual = atual.proximo

        novo.proximo = atual.proximo
        atual.proximo = novo

    lista.quantidade += 1

def imprimir(lista):
    atual = lista.primeiro

    if atual == None:
        print("Playlist vazia")
        return

    while atual != None:
        m = atual.musica

        print(
            f"ID: {m.id} | "
            f"{m.titulo} | "
            f"{m.artista} | "
            f"{m.album} | "
            f"{m.duracao} min"
        )

        atual = atual.proximo


def buscar(lista, id):
    atual = lista.primeiro

    while atual != None:
        if atual.musica.id == id:
            return atual.musica

        atual = atual.proximo

    return None

def buscar_artista(lista, artista):
    atual = lista.primeiro
    encontrou = False

    while atual != None:
        if atual.musica.artista.lower() == artista.lower():
            print(atual.musica.titulo)
            encontrou = True

        atual = atual.proximo

    if encontrou == False:
        print("Nenhuma musica encontrada")

def remover(lista, id):
    atual = lista.primeiro
    anterior = None

    while atual != None:

        if atual.musica.id == id:

            if anterior == None:
                lista.primeiro = atual.proximo
            else:
                anterior.proximo = atual.proximo

            lista.quantidade -= 1
            return True

        anterior = atual
        atual = atual.proximo

    return False

def duracao_total(lista):
    atual = lista.primeiro
    total = 0

    while atual != None:
        total += atual.musica.duracao
        atual = atual.proximo

    return total

def cadastrar_musica():
    id = int(input("ID: "))
    titulo = input("Titulo: ")
    artista = input("Artista: ")
    album = input("Album: ")
    duracao = float(input("Duracao em minutos: "))

    return Musica(id, titulo, artista, album, duracao)

# PROGRAMA

playlist = inicializar_lista()

while True:

    print("\n--- PLAYLIST ---")
    print("1 - Inserir no inicio")
    print("2 - Inserir no final")
    print("3 - Inserir em uma posicao")
    print("4 - Mostrar playlist")
    print("5 - Buscar por ID")
    print("6 - Buscar por artista")
    print("7 - Remover")
    print("8 - Quantidade de musicas")
    print("9 - Duracao total")
    print("0 - Sair")

    opcao = int(input("Opcao: "))

    if opcao == 0:
        break

    elif opcao == 1:
        musica = cadastrar_musica()
        inserir(playlist, musica, 1)

    elif opcao == 2:
        musica = cadastrar_musica()
        inserir(playlist, musica)

    elif opcao == 3:
        musica = cadastrar_musica()
        posicao = int(input("Posicao: "))
        inserir(playlist, musica, posicao)

    elif opcao == 4:
        imprimir(playlist)

    elif opcao == 5:
        id = int(input("ID: "))
        musica = buscar(playlist, id)

        if musica == None:
            print("Musica nao encontrada")
        else:
            print(musica.titulo, "-", musica.artista)

    elif opcao == 6:
        artista = input("Artista: ")
        buscar_artista(playlist, artista)

    elif opcao == 7:
        id = int(input("ID: "))

        if remover(playlist, id):
            print("Musica removida")
        else:
            print("Musica nao encontrada")

    elif opcao == 8:
        print("Quantidade:", playlist.quantidade)

    elif opcao == 9:
        print("Duracao total:", duracao_total(playlist), "min")
