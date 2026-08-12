"""
Iterável -> str, range, etc (__iter__)
Iterador -> Quem sabe entregar um valor por vez 
-----------------------------------------------
next -> Me entregue o próximo valor
iter -> Me entregue seu intervalo
"""
# for letra in texto
texto = "Luiz" # Iterável
iterador = iter(texto) # Iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)