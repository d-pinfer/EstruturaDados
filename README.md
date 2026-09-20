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

---

## Operações da pilha

* `inicializar_pilha`: cria uma pilha vazia;
* `empilhar`: adiciona um disco ao topo;
* `desempilhar`: remove o disco do topo;
* `topo`: consulta o disco do topo;
* `imprimir`: exibe os discos da pilha.

---

## Como executar

É necessário utilizar **Python 3.10 ou superior**.

```bash
python E3_jogoTorreHanoi.py
```

ou:

```bash
python3 E3_jogoTorreHanoi.py
```

---

## Exemplo de execução

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

Movimento:

```text
Torre de origem: 1
Torre de destino: 2
```

Resultado:

```text
Movimento realizado: disco 1
Torre 1 -> Torre 2
```

---

## Testes realizados

| Nº | Teste                   | Resultado                                  |
| -- | ----------------------- | ------------------------------------------ |
| 1  | Inicializar pilha       | Pilha vazia criada corretamente            |
| 2  | Empilhar disco          | Disco passa a ocupar o topo                |
| 3  | Desempilhar disco       | Disco do topo é removido                   |
| 4  | Consultar topo          | Retorna o disco sem removê-lo              |
| 5  | Movimento válido        | Disco é transferido                        |
| 6  | Origem vazia            | Movimento bloqueado                        |
| 7  | Disco maior sobre menor | Movimento bloqueado                        |
| 8  | Origem igual ao destino | Movimento bloqueado                        |
| 9  | Contador                | Incrementado apenas em movimentos válidos  |
| 10 | Reiniciar partida       | Torres e contador retornam ao início       |
| 11 | Vitória                 | Jogo reconhece os quatro discos na Torre 3 |
| 12 | Solução mínima          | Vitória possível em `15` movimentos        |

Todos os testes apresentaram os resultados esperados.

---

# Atividade 4 — Fila: Jogo Genius

**Arquivo:** `E4_jogoGenius.py`

## Descrição

Nesta atividade foi desenvolvido um **Jogo Genius** utilizando uma fila dinâmica implementada com nós encadeados.

A cada rodada, uma nova cor é adicionada à sequência. O jogador deve repetir todas as cores na mesma ordem apresentada.

As cores utilizadas são:

* VERDE;
* VERMELHO;
* AZUL;
* AMARELO.

A sequência segue o princípio **FIFO (First In, First Out)**.

---

## Estruturas utilizadas

```text
No
├── cor
└── proximo
```

```text
Fila
├── inicio
├── fim
└── quantidade
```

---

## Operações da fila

* `inicializar_fila`: cria uma fila vazia;
* `enfileirar`: adiciona uma cor ao final;
* `desenfileirar`: remove a primeira cor;
* `frente`: consulta a primeira cor;
* `imprimir`: exibe a sequência.

---

## Como executar

É necessário possuir **Python 3.10 ou superior**.

```bash
python E4_jogoGenius.py
```

ou:

```bash
python3 E4_jogoGenius.py
```

---

## Exemplo de execução

```text
================================
           RODADA 1
================================

Memorize a sequencia:
VERDE

Repita a sequencia:
Cor: verde

Voce acertou!
Pontuacao: 1
```

Próxima rodada:

```text
VERDE -> AZUL

Cor: verde
Cor: azul

Voce acertou!
Pontuacao: 2
```

---

## Testes realizados

| Nº | Teste                   | Resultado                          |
| -- | ----------------------- | ---------------------------------- |
| 1  | Inicializar fila        | Fila vazia criada corretamente     |
| 2  | Enfileirar primeira cor | `inicio` e `fim` apontam para o nó |
| 3  | Enfileirar várias cores | Ordem de inserção é mantida        |
| 4  | Consultar frente        | Retorna a primeira cor             |
| 5  | Desenfileirar           | Remove a primeira cor              |
| 6  | Fila vazia              | Retorna `None`                     |
| 7  | Imprimir sequência      | Exibe cores na ordem correta       |
| 8  | Adicionar cor           | Nova cor é adicionada ao final     |
| 9  | Acertar sequência       | Avança para próxima rodada         |
| 10 | Pontuação               | Aumenta após acerto                |
| 11 | Errar sequência         | Partida é encerrada                |
| 12 | Reiniciar               | Fila e pontuação voltam ao início  |
| 13 | Encerrar                | Programa finaliza corretamente     |

Todos os testes apresentaram os resultados esperados.

---

# Atividade 5 — Heap: Fila de Prioridade de Pedidos

**Arquivo:** `E5_filaPrioridadePedidos.py`

## Descrição

Nesta atividade foi desenvolvido um sistema de gerenciamento de pedidos utilizando um **Max-Heap**.

Cada pedido possui:

* ID;
* descrição;
* prioridade.

Quanto maior o valor da prioridade, maior a prioridade do pedido.

O Max-Heap mantém o pedido de maior prioridade na primeira posição do vetor.

Exemplo:

```text
[8, 5, 3, 2, 1]
```

Representação:

```text
        8
       / \
      5   3
     / \
    2   1
```

O Heap é armazenado utilizando um vetor e não utiliza o módulo `heapq`.

---

## Estruturas utilizadas

Cada pedido possui:

```text
Pedido
├── id
├── descricao
└── prioridade
```

O Heap possui:

```text
Heap
├── dados
├── tamanho
└── capacidade
```

O vetor possui capacidade inicial igual a `5`.

Quando o vetor fica cheio, sua capacidade é duplicada automaticamente.

---

## Relações entre os índices

Para um elemento localizado na posição `i`:

```text
pai      = (i - 1) // 2
esquerdo = 2 * i + 1
direito  = 2 * i + 2
```

Essas relações permitem representar a árvore do Heap dentro do vetor.

---

## Operações do Heap

### `inicializar_heap`

Cria um Heap vazio com capacidade inicial igual a `5`.

### `inserir`

Insere um novo pedido no final do vetor.

Após a inserção, o pedido é comparado com seu pai e realiza trocas enquanto possuir prioridade maior.

Dessa forma, o Heap é reorganizado automaticamente após cada inserção.

### `remover`

Remove e retorna o pedido localizado na raiz do Heap, que sempre corresponde ao pedido de maior prioridade.

Após a remoção, o último pedido ocupa a raiz e o Heap é reorganizado automaticamente.

### `max_heapfy`

Compara um elemento com seus filhos esquerdo e direito e realiza as trocas necessárias para restaurar a propriedade do Max-Heap.

### `construir`

Percorre os elementos internos do vetor e utiliza `max_heapfy` para organizar os pedidos como um Max-Heap.

### `print_heap`

Exibe os pedidos atualmente armazenados no Heap.

---

## Como executar

É necessário possuir **Python 3.10 ou superior**, pois o programa utiliza `match/case`.

No terminal:

```bash
python E5_filaPrioridadePedidos.py
```

ou:

```bash
python3 E5_filaPrioridadePedidos.py
```

---

## Menu do programa

```text
===== SISTEMA DE PEDIDOS =====
1 - Cadastrar pedido
2 - Atender pedido
3 - Exibir pedidos
4 - Exibir quantidade de pedidos
5 - Sair
```

---

## Exemplo de execução

Cadastro de pedidos:

```text
Escolha: 1
ID: 101
Descricao: Pedido de 10 produtos
Prioridade: 2

Escolha: 1
ID: 102
Descricao: Pedido de 5 produtos
Prioridade: 5

Escolha: 1
ID: 103
Descricao: Pedido de 20 produtos
Prioridade: 3

Escolha: 1
ID: 104
Descricao: Pedido urgente
Prioridade: 8
```

Ao exibir os pedidos:

```text
Escolha: 3

ID: 104 | Pedido urgente | Prioridade: 8
ID: 102 | Pedido de 5 produtos | Prioridade: 5
ID: 103 | Pedido de 20 produtos | Prioridade: 3
ID: 101 | Pedido de 10 produtos | Prioridade: 2
```

O pedido de maior prioridade permanece na raiz do Heap.

---

## Atendimento de pedido

Ao selecionar:

```text
Escolha: 2
```

Resultado:

```text
Pedido atendido:
ID: 104
Descricao: Pedido urgente
Prioridade: 8
```

Após a remoção, o Heap é reorganizado automaticamente e o próximo pedido de maior prioridade passa a ocupar a raiz.

---

## Aumento da capacidade

O Heap inicia com capacidade para `5` pedidos.

Caso essa capacidade seja atingida:

```text
5 -> 10 -> 20 -> 40
```

A capacidade do vetor é duplicada automaticamente, permitindo a inclusão de novos pedidos.

---

## Testes realizados

| Nº | Teste                              | Resultado                                                       |
| -- | ---------------------------------- | --------------------------------------------------------------- |
| 1  | Inicializar Heap                   | Heap criado com tamanho `0` e capacidade `5`                    |
| 2  | Inserir primeiro pedido            | Pedido ocupa a raiz                                             |
| 3  | Inserir pedido de maior prioridade | Novo pedido sobe até a posição correta                          |
| 4  | Inserir vários pedidos             | Propriedade do Max-Heap é mantida                               |
| 5  | Remover pedido                     | Pedido de maior prioridade é removido                           |
| 6  | Reorganizar após remoção           | Próximo maior pedido passa para a raiz                          |
| 7  | Remover Heap vazio                 | Retorna `None`                                                  |
| 8  | `max_heapfy`                       | Elementos são reorganizados corretamente                        |
| 9  | Construir Heap                     | Vetor é reorganizado como Max-Heap                              |
| 10 | Exibir pedidos                     | Pedidos armazenados são apresentados                            |
| 11 | Verificar quantidade               | `tamanho` corresponde ao total de pedidos                       |
| 12 | Aumentar capacidade                | Capacidade é duplicada ao preencher o vetor                     |
| 13 | Continuar inserindo                | Novos pedidos podem ser cadastrados normalmente                 |
| 14 | Atender todos os pedidos           | Pedidos são removidos do maior para o menor nível de prioridade |
| 15 | Sair                               | Programa é encerrado corretamente                               |

Todos os testes apresentaram os resultados esperados.

---

# Atividade 6 — Tabelas Hash

**Arquivo:** `E6_tabelaHash.py`

## Descrição

Nesta atividade foi implementada uma **Tabela Hash** utilizando a função:

```text
h(k) = k mod 7
```

A tabela possui `7` posições e utiliza **encadeamento externo** para tratar colisões.

O conjunto utilizado foi:

```text
{190, 322, 172, 89, 13, 4, 769, 61, 15, 76}
```

Quando dois ou mais valores resultam na mesma posição da função hash, eles são armazenados em nós encadeados.

Exemplo:

```text
190 % 7 = 1
15 % 7 = 1
```

Resultado:

```text
1 -> 190 -> 15
```

---

## Estruturas utilizadas

Cada elemento da tabela é armazenado em um nó:

```text
No
├── valor
└── proximo
```

A tabela Hash possui:

```text
Hash
├── tabela
└── quantidade
```

A tabela possui tamanho fixo igual a `7`.

---

## Função Hash

A função utilizada é:

```python
def funcao_hash(valor):
    return valor % TAMANHO
```

Como:

```text
TAMANHO = 7
```

a posição de cada valor é determinada pelo resto da divisão por `7`.

| Valor |   Cálculo | Posição |
| ----: | --------: | ------: |
|   190 | `190 % 7` |       1 |
|   322 | `322 % 7` |       0 |
|   172 | `172 % 7` |       4 |
|    89 |  `89 % 7` |       5 |
|    13 |  `13 % 7` |       6 |
|     4 |   `4 % 7` |       4 |
|   769 | `769 % 7` |       6 |
|    61 |  `61 % 7` |       5 |
|    15 |  `15 % 7` |       1 |
|    76 |  `76 % 7` |       6 |

---

## Tabela Hash resultante

Após inserir todos os valores:

```text
0 -> 322
1 -> 190 15
2 ->
3 ->
4 -> 172 4
5 -> 89 61
6 -> 13 769 76
```

As posições `1`, `4`, `5` e `6` apresentam colisões, resolvidas por encadeamento externo.

---

## Operações implementadas

### `funcao_hash`

Calcula a posição do valor na tabela através da operação:

```text
valor % 7
```

### `inserir`

Calcula a posição do valor e cria um novo nó.

Caso a posição já possua elementos, o novo nó é colocado no final da lista encadeada.

### `buscar`

Calcula a posição do valor e percorre apenas os nós daquela posição até encontrar o elemento.

Retorna `True` quando encontra e `False` quando não encontra.

### `remover`

Localiza o valor dentro da posição correspondente e ajusta o encadeamento para removê-lo.

### `imprimir`

Percorre todas as posições da tabela e mostra os valores armazenados.

### `fator_carga`

Calcula o fator de carga utilizando:

```text
quantidade de elementos / tamanho da tabela
```

---

## Como executar

No terminal:

```bash
python E6_tabelaHash.py
```

ou:

```bash
python3 E6_tabelaHash.py
```

---

## Exemplo de execução

Tabela inicial:

```text
--- TABELA HASH ---
0 -> 322
1 -> 190 15
2 ->
3 ->
4 -> 172 4
5 -> 89 61
6 -> 13 769 76
```

Fator de carga:

```text
Fator de carga: 1.43
```

---

## Exemplo de remoção

O programa remove o valor `769`.

Antes:

```text
6 -> 13 769 76
```

Depois:

```text
6 -> 13 76
```

Saída:

```text
Removendo 769...
```

A tabela passa a ser:

```text
0 -> 322
1 -> 190 15
2 ->
3 ->
4 -> 172 4
5 -> 89 61
6 -> 13 76
```

---

## Exemplo de inserção

Após a remoção, o programa insere o valor `67`.

A posição é calculada por:

```text
67 % 7 = 4
```

Como já existem elementos na posição `4`, ocorre uma colisão.

Antes:

```text
4 -> 172 4
```

Depois:

```text
4 -> 172 4 67
```

---

## Fator de carga

Antes das operações de remoção e nova inserção existem `10` elementos em uma tabela de tamanho `7`.

```text
Fator de carga = 10 / 7
Fator de carga = 1.43
```

O fator de carga pode ser maior que `1` porque o tratamento de colisões é realizado por encadeamento externo.

---

## Testes realizados

| Nº | Teste                            | Resultado                                   |
| -- | -------------------------------- | ------------------------------------------- |
| 1  | Criar tabela Hash                | Tabela criada com `7` posições              |
| 2  | Calcular `190 % 7`               | Retorna posição `1`                         |
| 3  | Inserir primeiro valor           | Valor armazenado na posição correta         |
| 4  | Inserir vários valores           | Valores distribuídos pela função Hash       |
| 5  | Colisão entre `190` e `15`       | Ambos ficam encadeados na posição `1`       |
| 6  | Colisão na posição `6`           | `13`, `769` e `76` ficam encadeados         |
| 7  | Buscar valor existente           | Retorna `True`                              |
| 8  | Buscar valor inexistente         | Retorna `False`                             |
| 9  | Remover `769`                    | Valor é retirado da posição `6`             |
| 10 | Manter encadeamento após remoção | Posição `6` passa a conter `13 76`          |
| 11 | Inserir `67`                     | Valor é inserido na posição `4`             |
| 12 | Calcular fator de carga          | Resultado inicial igual a `1.43`            |
| 13 | Imprimir tabela                  | Todas as posições são exibidas corretamente |

Os testes apresentaram os resultados esperados.

---

# Estrutura do repositório

```text
/
├── E1_bibliotecasMath.py
├── E2_playlist.py
├── E3_jogoTorreHanoi.py
├── E4_jogoGenius.py
├── E5_filaPrioridadePedidos.py
├── E6_tabelaHash.py
└── README.md
```

As próximas atividades serão adicionadas neste mesmo repositório e documentadas neste README.

