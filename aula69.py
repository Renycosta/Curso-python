"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
def imprimir():
    print("Várias")

imprimir()


def funcao_parametros(a, b, c):
    print(a, b, c)

funcao_parametros(1, 2, 3)
funcao_parametros(4, 5, 6)


def saudacao(nome="Sem nome"):
    print(f"Olá {nome}")

saudacao("Luiz")
saudacao("Maria")
saudacao()