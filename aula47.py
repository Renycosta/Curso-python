"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "perfume"
letras_encontradas = ""

contador = 0

while True:

    palavra_formatada = ""

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue 

    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] in letras_encontradas:
            palavra_formatada += palavra_secreta[i] 
        elif letra in palavra_secreta[i]:
            palavra_formatada += letra
            letras_encontradas += letra
        else:    
            palavra_formatada += "*"

    if palavra_formatada == palavra_secreta:
        os.system("clear")
        print("VOCÊ GANHOU PARABÉNS!!")
        print(f"A palavra era: {palavra_secreta}")
        print(f"Tentivas {contador}")
        letras_encontradas = ""
        contador = 0
        continue

    contador += 1

    print(palavra_formatada)