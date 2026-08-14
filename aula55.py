"""
Introdução ao desempacotamento + tuples
"""
nomes = ["Maria", "Helena", "Luiz"]
nome1, nome2, nome3 = nomes
print(nome2)

frutas = ["Laranja", "Maça", "Banana"]
fruta1, *resto = frutas
print(fruta1)

fruta_1, *_ = frutas

_, fruta2, *_ = frutas