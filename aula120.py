# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    nova_lista = []

    for i, valor in enumerate(l1):
        nova_lista.append((valor, l2[i]))

    return nova_lista

nova = zipper(lista1, lista2)
print(nova)