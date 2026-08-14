# Desempacotamento em chamadas
# de métodos e funções
string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, 4, "Eduarda"]
tupla = "Python", "é", "legal"
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]

p, b, *_, ap,  u = lista
print(p, u, ap)

print(*lista)
print(*string)
print(*tupla)

# for nome in lista:
#     print(nome, end=" ", sep=" ")

print(*salas, sep="\n")