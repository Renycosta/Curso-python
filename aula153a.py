# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João", 35)

def fazer_dump1():
    with open("aula153_classe_dado_1", "w", encoding="utf-8") as arquivo:
        json.dump(p1.__dict__, arquivo, ensure_ascii=False, indent=4)

p2 = Pessoa("Aliene", 25)
p3 = Pessoa("Fernanda", 10)
p4 = Pessoa("Angelo", 40)
bd = [vars(p2), vars(p3), vars(p4)]

def fazer_dump2():
    with open("aula153_classe_dados", "w", encoding="utf-8") as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    print("Ele é o main")
    fazer_dump1()
    fazer_dump2()