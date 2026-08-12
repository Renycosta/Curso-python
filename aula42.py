frase = "O Python é uma linguagem de programação "\
    "multiparadigma. "\
    "Python foi criado por Guido van Rossum."

contador = 0
quantidade = 0
letra = ""

while contador < len(frase):
    letra_atual = frase[contador]
    quantidade_atual = frase.count(letra_atual)

    if  quantidade_atual > quantidade and letra_atual != " ":
        quantidade = quantidade_atual
        letra = letra_atual
    contador += 1

print(f"A letra que mais apareceu foi: '{letra}' que apareceu: {quantidade}")