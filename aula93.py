# List comprehension em Python
# List comprehension é uma forma rapida de criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero for numero in range(10)]
lista2 = [numero * 2 for numero in range(10)]
print(lista)
print(lista2)