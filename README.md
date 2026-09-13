# FarmTech Solutions - Sistema de Gestão de Plantio

Projeto desenvolvido para a disciplina de Fundamentos de Python (FIAP - Fase 1),
simulando um sistema usado pela startup FarmTech Solutions para apoiar a gestão
de uma fazenda que está migrando para a Agricultura Digital.

O sistema permite cadastrar culturas, calcular a área de plantio e o volume de
insumos necessário para cada uma, além de listar, atualizar e deletar os
registros feitos.

## Culturas suportadas

| Cultura | Figura geométrica usada no cálculo de área | Fórmula |
|---|---|---|
| Café | Retângulo | `área = largura × comprimento` |
| Cana-de-açúcar | Triângulo | `área = (base × altura) / 2` |

## Cálculo de insumos

Para cada registro, além da área, o usuário informa o nome do insumo e a dose
aplicada (em mL por m²). O sistema converte automaticamente para litros:

```
total_litros = (área × dose) / 1000
```

## Funcionalidades (menu)

O programa roda em loop até que a opção "Sair" seja escolhida:

1. **Cadastrar Cultura** — solicita o tipo de cultura (Café ou Cana), as
   medidas necessárias, o insumo e a dose, calcula a área e o total de
   litros, e guarda tudo nos vetores.
2. **Listar Dados** — imprime todos os registros cadastrados, com a posição
   de cada um no vetor.
3. **Atualizar registro** — lista os registros, pede a posição a alterar e
   substitui os dados naquele índice.
4. **Deletar registro** — lista os registros, pede a posição a remover e
   apaga o item das 4 listas.
5. **Sair** — encerra o programa.

Entradas numéricas inválidas (texto onde se espera número) não derrubam o
programa: o usuário é avisado e pode digitar novamente.

## Estrutura de dados

Os dados são organizados em 4 vetores (listas) paralelos, onde a mesma
posição `i` em cada lista pertence ao mesmo registro:

```python
culturas = []   # nome da cultura (Cafe / Cana)
areas    = []   # área calculada em m²
insumos  = []   # nome do insumo aplicado
litros   = []   # volume total de insumo em litros
```

## Como executar

Pré-requisito: Python 3.10+ (o projeto usa `match/case`, disponível a partir
do Python 3.10).

```bash
python Farmtech.py
```

Depois é só seguir o menu exibido no terminal.

## Estrutura do repositório

```
farmtech/
├── Farmtech.py   # aplicação principal em Python
└── README.md
```

## Equipe

Desenvolvido pelo grupo da FarmTech Solutions - Fase 1 (FIAP).

## Próximos passos

- Script em R para cálculo de estatísticas básicas (média e desvio padrão)
  a partir dos dados gerados pelo Python.
- Integração em R com uma API meteorológica pública.
- Resumo do artigo indicado pela disciplina de Formação Social.
- Vídeo de demonstração no YouTube (link a ser adicionado em arquivo `.txt`).
