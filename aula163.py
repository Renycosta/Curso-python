# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._Fabricante = None

        @property
        def motor(self):
            return self._motor

        @motor.setter
        def motor(self, motor):
            self._motor = motor

        @property
        def fabricante(self):
            return self._fabricante

        @fabricante.setter
        def fabricante(self, fabricante):
            self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

c1, c2, c3, c4, c5 = Carro("Carro1"), Carro("Carro2"), Carro("Carro3"), Carro("Carro4"), Carro("Carro5")
m1, m2 = Motor("Motor1"), Motor("Motor2")
f1, f2 = Fabricante("Fabricante1"), Fabricante("Fabricante2")

c1.motor, c2.motor, c3.motor = m1, m1, m1
c1.fabricante, c2.fabricante, c3.fabricante, = f2, f2, f2

c4.motor, c5.motor = m2, m2
c4.fabricante, c5.fabricante = f1, f1

print(c1.nome, c1.motor.nome, c1.fabricante.nome)
print(c2.nome, c2.motor.nome, c2.fabricante.nome)
print(c3.nome, c3.motor.nome, c3.fabricante.nome)
print(c4.nome, c4.motor.nome, c4.fabricante.nome)
print(c5.nome, c5.motor.nome, c5.fabricante.nome)