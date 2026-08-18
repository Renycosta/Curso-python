# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

print(pessoa.__len__())
print(len(pessoa))

print(pessoa.keys())
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))

print(pessoa.values())
print(tuple(pessoa.values()))
print(list(pessoa.values()))

print(pessoa.items())
print(tuple(pessoa.items()))
print(list(pessoa.items()))

pessoa.setdefault("idade", 18)
print(pessoa["idadef"])