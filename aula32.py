"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")

try:
    numero_int = int(numero)
    par_ou_impar = numero_int % 2

    if par_ou_impar == 0:
        print(f"O número {numero_int} é par")
    else:
        print(f"O número {numero_int} é impar")
except:
    print("Isso não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input("Digite a hora: ")
horario_int = int(horario)

if horario_int >= 0 and horario_int <= 11:
    print("Bom dia")
elif horario_int >= 12 and horario_int <= 17:
    print("Boa tarde")
else:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) > 6:
    print("Seu nome é muito grande")
else:
    print("Seu nome é normal")