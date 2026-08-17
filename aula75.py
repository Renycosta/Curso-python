# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável
def multiplica(*args):
    acumulador = 1
    for num in args:
        acumulador *= num
    return acumulador

total = multiplica(2, 8, 4, 6)
print(total)

# Crie uma função fala se um número é par ou impar
# Retorne se o número é par ou impar
def par_ou_impar(num):
    if num % 2 == 0:
        return f"{num} é par"
    return f"{num} é impar"

numero1 = par_ou_impar(1)
numero2 = par_ou_impar(2)
print(numero1)
print(numero2)