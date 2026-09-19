# # Estruturas de Dados

Repositório destinado às atividades práticas da disciplina de Estruturas de Dados.

As atividades são desenvolvidas em **Python**. Este README será atualizado conforme novas atividades forem adicionadas ao repositório.

---

# Atividade 1 — Arrays e Similaridade de Cosseno

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

# Testes realizados

## Teste 1 — Inserção e impressão

Entrada:

```text
[1.0, 2.0, 3.0]
```

Resultado esperado:

```text
[1.0, 2.0, 3.0]
```

---

## Teste 2 — Busca e remoção

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

---

## Teste 3 — Operações matemáticas

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

---

## Teste 4 — Similaridade de cosseno

```text
A = [1.0, 2.0, 3.0]
B = [4.0, 5.0, 6.0]
```

Resultado:

```text
0.9746
```

---

## Teste 5 — Vetor nulo

```text
A = [0.0, 0.0, 0.0]
B = [1.0, 2.0, 3.0]
```

Resultado esperado:

```text
Operacao invalida
```

---

# Estrutura do repositório

```text
/
├── E1_bibliotecasMath.py
└── README.md
```

As próximas atividades serão adicionadas neste mesmo repositório e documentadas neste README.
