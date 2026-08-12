"""
Iterando strings com while
"""
#       012345678910
nome = "Luiz Otavio" # Iteraveis
tamanho_nome = len(nome)
print(nome)
print(nome[3])
print(tamanho_nome)

nova_string = ""
contador = 0

while contador < tamanho_nome:
    nova_string += "*"
    nova_string += nome[contador]
    contador += 1

print(nova_string)