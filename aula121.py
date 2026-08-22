"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]


def zipper(l1, l2):
    maior = []
    menor = []

    if len(l1) > len(l2):
        maior = l1.copy()
        menor = l2.copy()
    else:
        maior = l2.copy()
        menor = l1.copy()

    nova_lista = [valor + maior[i] for i, valor in enumerate(menor)]
    return nova_lista

nova = zipper(lista_b, lista_a)
print(nova)

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)