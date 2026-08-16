"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    # Definição
    print(f"{x=} y={y}", "|", "x + y =", x + y)

soma(1, 2)
soma(2, 1)
soma(y=2, x=1)

def soma3(x, y, z):
    print(f"{x=} y={y} z={z}", "|", "x + y + z =", x + y)

soma3(1, 2, 3)
soma3(x=1, y=2, z=3)
soma3(1, y=2, z=3)