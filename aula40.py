""" Calculadora com while """
while True:
    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair:
        break

    num1 = input("Digite o primeiro número: ")
    operador = input("Digite o operador (+-*/): ")
    num2 = input("Digite o segundo número: ")

    try:
        num1_int = int(num1)
        num2_int = int(num2)

        if operador == "+":
            print(num1_int + num2_int)
        elif operador == "-":
            print(num1_int - num2_int)
        elif operador == "*":
            print(num1_int * num2_int)
        elif operador == "/":
            print(num1_int / num2_int)
        else:
            print("Você não digitou um operador")
    except:
        print("Você não digitou um número")

print("Saiu do programa")