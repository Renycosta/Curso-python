# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print("chamou upper")
#         retorno = super().upper()
#         print("depois do upper")
#         return retorno

# string = MinhaString("luiz")
# print(string.upper())

class A:
    atributo_A = "valor A"

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print("A")

class B(A):
    atributo_B = "valor B"

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print("B")

class C(B):
    atributo_C = "valor C"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super(A, self).metodo() # object
        super(B, self).metodo() # A
        super(C, self).metodo() # super().metodo() # B
        print("C")

c = C("Atributo", "Qualquer")
print(c.atributo)
print(c.atributo_A)
print(c.atributo_B)
print(c.atributo_C)
c.metodo()