# Estruturas de Dados

Repositório destinado às atividades práticas da disciplina de Estruturas de Dados.

As atividades são desenvolvidas em **Python**. Este README será atualizado conforme novas atividades forem adicionadas ao repositório.

---

# Atividade 1 — Array: Biblioteca matemática

**Arquivo:** `E1_bibliotecasMath.py`

## Descrição

Nesta atividade foi desenvolvida uma aplicação para armazenar e manipular vetores de números reais utilizando arrays.

Foram implementadas as seguintes operações:

* inicialização;
* inserção;
* impressão;
* busca;
* remoção;
* multiplicação por escalar;
* soma de vetores;
* produto escalar;
* norma euclidiana;
* similaridade de cosseno.

---

## Linguagem utilizada

Python 3.

Foi utilizada a biblioteca padrão `math`.

---

## Como executar

No terminal:

```bash
python E1_bibliotecasMath.py
```

ou:

```bash
python3 E1_bibliotecasMath.py
```

---

## Exemplo de execução

Entrada:

```text
Tamanho dos vetores: 3

Digite o vetor A:
1
2
3

Digite o vetor B:
4
5
6

Digite um escalar:
2
```

Saída:

```text
Vetor A: [1.0, 2.0, 3.0]
Vetor B: [4.0, 5.0, 6.0]
Multiplicacao por escalar: [2.0, 4.0, 6.0]
Soma: [5.0, 7.0, 9.0]
Produto escalar: 32.0
Norma de A: 3.7417
Similaridade: 0.9746
```

---

## Testes realizados

| Nº | Teste                   | Entrada                           | Resultado           |
| -- | ----------------------- | --------------------------------- | ------------------- |
| 1  | Inserção e impressão    | `[1.0, 2.0, 3.0]`                 | `[1.0, 2.0, 3.0]`   |
| 2  | Busca                   | Buscar `2.0` em `[1.0, 2.0, 3.0]` | Índice `1`          |
| 3  | Remoção                 | Remover `2.0`                     | `[1.0, 3.0]`        |
| 4  | Soma                    | A = `[1,2,3]`, B = `[4,5,6]`      | `[5.0, 7.0, 9.0]`   |
| 5  | Produto escalar         | A = `[1,2,3]`, B = `[4,5,6]`      | `32.0`              |
| 6  | Norma                   | A = `[1,2,3]`                     | `3.7417`            |
| 7  | Similaridade de cosseno | A = `[1,2,3]`, B = `[4,5,6]`      | `0.9746`            |
| 8  | Vetor nulo              | A = `[0,0,0]`                     | `Operacao invalida` |

Os testes apresentaram os resultados esperados.

---

# Atividade 2 — Lista Encadeada: Playlist

**Arquivo:** `E2_playlist.py`

## Descrição

Nesta atividade foi desenvolvida uma aplicação para gerenciamento de uma playlist utilizando uma **lista dinâmica encadeada**.

Cada música é armazenada em um nó da lista e possui as seguintes informações:

* ID;
* título;
* artista;
* álbum;
* duração.

Cada nó possui uma referência para o próximo nó da lista.

A estrutura utilizada segue o formato:

```text
[Musica 1] -> [Musica 2] -> [Musica 3] -> None
```

A playlist não utiliza uma lista pronta do Python para armazenar as músicas. O encadeamento é realizado manualmente por meio da referência `proximo`.

---

## Estruturas utilizadas

A classe `Musica` armazena os dados de cada música.

A classe `No` representa cada elemento da lista encadeada:

```text
No
├── musica
└── proximo
```

A classe `Lista` representa a playlist:

```text
Lista
├── primeiro
└── quantidade
```

---

## Operações implementadas

As operações principais da lista encadeada são:

* `inicializar_lista`;
* `inserir`;
* `imprimir`;
* `buscar`;
* `remover`.

Também foram implementadas:

* cadastro de música;
* inserção no início;
* inserção no final;
* inserção em posição determinada;
* busca por ID;
* busca por artista;
* quantidade de músicas;
* cálculo da duração total da playlist.

---

## Como executar

No terminal:

```bash
python E2_playlist.py
```

ou:

```bash
python3 E2_playlist.py
```

---

## Menu do programa

```text
--- PLAYLIST ---
1 - Inserir no inicio
2 - Inserir no final
3 - Inserir em uma posicao
4 - Mostrar playlist
5 - Buscar por ID
6 - Buscar por artista
7 - Remover
8 - Quantidade de musicas
9 - Duracao total
0 - Sair
```

---

## Exemplo de execução

Cadastro de duas músicas:

```text
Opcao: 2

ID: 1
Titulo: Numb
Artista: Linkin Park
Album: Meteora
Duracao em minutos: 3.05

Opcao: 2

ID: 2
Titulo: In The End
Artista: Linkin Park
Album: Hybrid Theory
Duracao em minutos: 3.36
```

Exibição da playlist:

```text
Opcao: 4

ID: 1 | Numb | Linkin Park | Meteora | 3.05 min
ID: 2 | In The End | Linkin Park | Hybrid Theory | 3.36 min
```

Quantidade:

```text
Opcao: 8
Quantidade: 2
```

Duração total:

```text
Opcao: 9
Duracao total: 6.41 min
```

---

## Testes realizados

| Nº | Teste                        | Resultado                                   |
| -- | ---------------------------- | ------------------------------------------- |
| 1  | Criar playlist vazia         | `primeiro = None` e quantidade `0`          |
| 2  | Inserir primeira música      | Música passa a ser o primeiro nó            |
| 3  | Inserir várias músicas       | Músicas permanecem encadeadas               |
| 4  | Inserir no início            | Nova música passa a ser a primeira          |
| 5  | Inserir no final             | Nova música passa a ser a última            |
| 6  | Inserir no meio              | Música é inserida na posição informada      |
| 7  | Buscar música existente      | Música encontrada pelo ID                   |
| 8  | Buscar música inexistente    | Retorna `None`                              |
| 9  | Buscar por artista           | Exibe músicas do artista informado          |
| 10 | Remover primeira música      | Segundo nó passa a ser o primeiro           |
| 11 | Remover música intermediária | Encadeamento é ajustado corretamente        |
| 12 | Remover última música        | Nó anterior passa a apontar para `None`     |
| 13 | Remover única música         | Playlist fica vazia                         |
| 14 | Remover música inexistente   | Playlist permanece inalterada               |
| 15 | Verificar quantidade         | Quantidade corresponde ao número de músicas |
| 16 | Calcular duração total       | Durações são somadas corretamente           |

Os testes apresentaram os resultados esperados.

---

# Atividade 3 — Pilha: Jogo Torre de Hanói

**Arquivo:** `E3_jogoTorreHanoi.py`

## Descrição

Nesta atividade foi desenvolvido o jogo **Torre de Hanói** utilizando pilhas dinâmicas implementadas com nós encadeados.

O jogo possui três torres e quatro discos.

Inicialmente os discos ficam na primeira torre, organizados do maior para o menor, sendo o menor disco localizado no topo da pilha.

```text
Torre 1: [ 1 2 3 4 ]
Torre 2: [ vazia ]
Torre 3: [ vazia ]
```

O objetivo é mover todos os discos para a Torre 3 respeitando as seguintes regras:

* apenas o disco do topo pode ser movimentado;
* apenas um disco pode ser movimentado por vez;
* um disco maior não pode ser colocado sobre um disco menor.

Cada torre é representada por uma pilha dinâmica encadeada.

---

## Estruturas utilizadas

Cada disco é armazenado em um nó:

```text
No
├── disco
└── proximo
```

Cada torre utiliza uma pilha:

```text
Pilha
├── topo
└── quantidade
```

Os nós são ligados pela referência `proximo`.

Não é utilizada uma lista pronta do Python para armazenar os discos.

---

## Operações da pilha

As operações implementadas são:

### `inicializar_pilha`

Cria uma nova pilha vazia.

```text
topo = None
quantidade = 0
```

### `empilhar`

Adiciona um novo disco no topo da pilha.

O novo nó passa a apontar para o antigo topo.

### `desempilhar`

Remove o disco localizado no topo da pilha e retorna seu valor.

A referência `topo` passa a apontar para o próximo nó.

### `topo`

Retorna o disco localizado no topo da pilha sem removê-lo.

### `imprimir`

Percorre os nós da pilha e mostra os discos armazenados.

---

## Funcionalidades implementadas

O jogo permite:

* iniciar uma nova partida;
* visualizar as três torres;
* selecionar uma torre de origem;
* selecionar uma torre de destino;
* realizar movimentos válidos;
* impedir movimentos inválidos;
* visualizar o número de movimentos;
* reiniciar a partida;
* encerrar o jogo;
* identificar quando o jogador venceu.

---

## Como executar

É necessário utilizar **Python 3.10 ou superior**, pois o programa utiliza `match/case`.

No terminal:

```bash
python E3_jogoTorreHanoi.py
```

ou:

```bash
python3 E3_jogoTorreHanoi.py
```

---

## Menu do jogo

```text
================================
        TORRE DE HANOI
================================
Torre 1: [ 1 2 3 4 ]
Torre 2: [ vazia ]
Torre 3: [ vazia ]
================================

Movimentos realizados: 0

--------- MENU ---------
1 - Fazer movimento
2 - Reiniciar partida
0 - Sair
------------------------
```

---

## Exemplo de execução

Estado inicial:

```text
Torre 1: [ 1 2 3 4 ]
Torre 2: [ vazia ]
Torre 3: [ vazia ]
```

Movimento:

```text
Escolha uma opcao: 1

Torre de origem (1, 2 ou 3): 1
Torre de destino (1, 2 ou 3): 2
```

Resultado:

```text
Movimento realizado: disco 1
Torre 1 -> Torre 2
```

Novo estado:

```text
Torre 1: [ 2 3 4 ]
Torre 2: [ 1 ]
Torre 3: [ vazia ]
```

---

## Exemplo de movimento inválido

Tentativa de colocar um disco maior sobre um menor:

```text
Torre de origem (1, 2 ou 3): 1
Torre de destino (1, 2 ou 3): 2
```

Caso o disco da Torre 1 seja maior que o disco localizado no topo da Torre 2:

```text
[ERRO] Um disco maior nao pode ficar sobre um menor!
```

O movimento não é realizado e o contador permanece com o mesmo valor.

---

## Condição de vitória

O jogador vence quando os quatro discos estiverem na Torre 3.

Estado final:

```text
Torre 1: [ vazia ]
Torre 2: [ vazia ]
Torre 3: [ 1 2 3 4 ]
```

Saída:

```text
********************************
          VOCE VENCEU!
********************************
Total de movimentos: 15
********************************
```

Para quatro discos, a solução mínima utiliza **15 movimentos**.

---

## Testes realizados

| Nº | Teste                   | Resultado                                                            |
| -- | ----------------------- | -------------------------------------------------------------------- |
| 1  | Inicializar pilha       | Pilha criada com `topo = None` e quantidade `0`                      |
| 2  | Empilhar disco          | Disco passa a ocupar o topo                                          |
| 3  | Desempilhar disco       | Disco do topo é removido                                             |
| 4  | Consultar topo          | Retorna o disco do topo sem removê-lo                                |
| 5  | Mostrar torres          | Exibe corretamente os discos das três pilhas                         |
| 6  | Movimento válido        | Disco é transferido entre as torres                                  |
| 7  | Origem vazia            | Movimento é bloqueado                                                |
| 8  | Disco maior sobre menor | Movimento é bloqueado                                                |
| 9  | Origem igual ao destino | Movimento é bloqueado                                                |
| 10 | Torre inválida          | Programa apresenta mensagem de erro                                  |
| 11 | Contador de movimentos  | É incrementado apenas em movimentos válidos                          |
| 12 | Reiniciar partida       | Torres retornam ao estado inicial e contador volta para `0`          |
| 13 | Encerrar jogo           | Programa finaliza corretamente                                       |
| 14 | Vitória                 | Ao colocar os quatro discos na Torre 3, o programa informa a vitória |
| 15 | Solução mínima          | Jogo pode ser concluído em `15` movimentos                           |

Todos os testes apresentaram os resultados esperados.

---

## Sequência utilizada para teste de vitória

Uma sequência válida para terminar o jogo com quatro discos é:

```text
1 -> 2
1 -> 3
2 -> 3
1 -> 2
3 -> 1
3 -> 2
1 -> 2
1 -> 3
2 -> 3
2 -> 1
3 -> 1
2 -> 3
1 -> 2
1 -> 3
2 -> 3
```

Resultado final:

```text
Torre 1: [ vazia ]
Torre 2: [ vazia ]
Torre 3: [ 1 2 3 4 ]

VOCE VENCEU!
Total de movimentos: 15
```

---

# Estrutura do repositório

```text
/
├── E1_bibliotecasMath.py
├── E2_playlist.py
├── E3_jogoTorreHanoi.py
└── README.md
```

As próximas atividades serão adicionadas neste mesmo repositório e documentadas neste README.

