"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
nome = "Luiz"
outra_variavel = nome
nome = "João"

print(nome)
print(outra_variavel)

lista_a = ["Luiz", "Maria"]
lista_b = lista_a
lista_a[0] = "Qualquer coisa"

print(lista_a)
print(lista_b)

lista_1 = ["Banana", "Maça"]
lista_2 = lista_a.copy()
lista_1[0] = "Qualquer coisa"

print(lista_1)
print(lista_2)