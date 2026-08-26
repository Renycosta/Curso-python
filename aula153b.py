import json

from aula153a import Pessoa, fazer_dump1, fazer_dump2

fazer_dump1()
fazer_dump2()

with open("aula153_classe_dado_1", "r", encoding="utf-8") as arquivo:
    dado_1 = json.load(arquivo)

p1 = Pessoa(**dado_1)

print(vars(p1))

with open("aula153_classe_dados", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

p2 = Pessoa(**dados[0])
p3 = Pessoa(**dados[1])
p4 = Pessoa(**dados[2])

print(vars(p2))
print(vars(p3))
print(vars(p4))