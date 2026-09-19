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

### Teste 1 — Inserção e impressão

Entrada:

```text
[1.0, 2.0, 3.0]
```

Resultado esperado:

```text
[1.0, 2.0, 3.0]
```

### Teste 2 — Busca e remoção

Vetor inicial:

```text
[1.0, 2.0, 3.0]
```

Busca pelo valor `2.0`:

```text
Índice 1
```

Após remover `2.0`:

```text
[1.0, 3.0]
```

### Teste 3 — Operações matemáticas

```text
A = [1.0, 2.0, 3.0]
B = [4.0, 5.0, 6.0]
```

Resultados:

```text
Soma: [5.0, 7.0, 9.0]
Produto escalar: 32.0
Norma de A: 3.7417
```

### Teste 4 — Similaridade de cosseno

```text
A = [1.0, 2.0, 3.0]
B = [4.0, 5.0, 6.0]
```

Resultado:

```text
0.9746
```

### Teste 5 — Vetor nulo

```text
A = [0.0, 0.0, 0.0]
B = [1.0, 2.0, 3.0]
```

Resultado esperado:

```text
Operacao invalida
```

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

Ao executar o programa, o seguinte menu é apresentado:

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

Inserção de uma música:

```text
Opcao: 2

ID: 1
Titulo: Numb
Artista: Linkin Park
Album: Meteora
Duracao em minutos: 3.05
```

Inserção de outra música:

```text
Opcao: 2

ID: 2
Titulo: In The End
Artista: Linkin Park
Album: Hybrid Theory
Duracao em minutos: 3.36
```

Ao selecionar a opção de mostrar a playlist:

```text
Opcao: 4
```

Saída:

```text
ID: 1 | Numb | Linkin Park | Meteora | 3.05 min
ID: 2 | In The End | Linkin Park | Hybrid Theory | 3.36 min
```

Quantidade de músicas:

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

Foram considerados os casos de teste obrigatórios da atividade.

| Nº | Teste                        | Resultado esperado                                      |
| -- | ---------------------------- | ------------------------------------------------------- |
| 1  | Criar playlist vazia         | Playlist criada com `primeiro = None` e quantidade `0`  |
| 2  | Inserir primeira música      | Música passa a ser o primeiro nó                        |
| 3  | Inserir várias músicas       | Todas permanecem encadeadas corretamente                |
| 4  | Inserir no início            | Nova música passa a ser o primeiro nó                   |
| 5  | Inserir no final             | Nova música é adicionada após o último nó               |
| 6  | Inserir no meio              | Música é inserida na posição informada                  |
| 7  | Buscar música existente      | Música correspondente ao ID é encontrada                |
| 8  | Buscar música inexistente    | Retorna `None` e informa que não foi encontrada         |
| 9  | Buscar por artista           | Exibe as músicas do artista informado                   |
| 10 | Remover primeira música      | O segundo nó passa a ser o primeiro                     |
| 11 | Remover música intermediária | O nó anterior passa a apontar para o próximo            |
| 12 | Remover última música        | O nó anterior passa a apontar para `None`               |
| 13 | Remover única música         | A playlist volta a ficar vazia                          |
| 14 | Remover música inexistente   | A lista permanece inalterada                            |
| 15 | Verificar quantidade         | O valor de `quantidade` corresponde ao total de músicas |
| 16 | Calcular duração total       | Soma corretamente a duração de todas as músicas         |

---

## Exemplos de testes

### Inserção no início

Playlist inicial:

```text
1 - Numb
2 - In The End
```

Inserindo uma música na posição inicial:

```text
3 - Faint
```

Resultado:

```text
3 - Faint
1 - Numb
2 - In The End
```

### Inserção no meio

Playlist:

```text
1 - Numb
2 - In The End
```

Inserção na posição 2:

```text
3 - Faint
```

Resultado:

```text
1 - Numb
3 - Faint
2 - In The End
```

### Busca por ID

Busca:

```text
ID: 2
```

Resultado:

```text
In The End - Linkin Park
```

### Busca por artista

Busca:

```text
Artista: Linkin Park
```

Resultado:

```text
Numb
In The End
```

### Remoção

Antes:

```text
1 - Numb
2 - In The End
3 - Faint
```

Removendo:

```text
ID: 2
```

Depois:

```text
1 - Numb
3 - Faint
```

### Quantidade e duração

Para duas músicas com durações `3.05` e `3.36`:

```text
Quantidade: 2
Duracao total: 6.41 min
```

---

# Estrutura do repositório

```text
/
├── E1_bibliotecasMath.py
├── E2_playlist.py
└── README.md
```

As próximas atividades serão adicionadas neste mesmo repositório e documentadas neste README.
