"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = "       Olha só que      , coisa interessante    "
listas_frases = frase.split(",")

listas_frases_fixed = []

for i, frase in enumerate(listas_frases):
    listas_frases_fixed.append(listas_frases[i].strip())

# print(listas_frases)
# print(listas_frases_fixed)

frases_unidas = "-".join(listas_frases_fixed)
print(frases_unidas)