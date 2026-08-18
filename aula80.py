# Manipulando chaves e valores em dicionários
pessoa = {}

pessoa["nome"] = "Luiz Otávio"
pessoa["sobrenome"] = "Miranda"

# chave = "sobrenome"
# pessoa[chave] = "Silva"
# print(pessoa[chave])

pessoa["nome"] = "Maria"
del pessoa["sobrenome"]

print(pessoa)
print(pessoa["nome"])

if pessoa.get("sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["sobrenome"])