# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

pessoas = [
    "João", "Joana", "Luiz", "Leticia",
]

camisetas = [
    ["preta", "branca"],
    ["p", "m", "g"],
    ["masculino", "feminino", "unisex"],
    ["algodão", "poliéster"],
]

print(list(combinations(pessoas, 2)))
print()
print(list(permutations(pessoas, 2)))
print()
print(list(product(*camisetas)))