"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista
"""
compras = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao.lower() == "i":
        valor = str(input("Valor: "))
        compras.append(valor)

    elif opcao.lower() == "a":
        apagar = int(input("Escolha o indice para apagar: "))
        try:
            del compras[apagar]
        except ValueError:
            print("Por favor digite um número int")
        except IndexError:
            print("Índice não existe na lista")
        except Exception:
            print("Erro desconhecido")

    elif opcao.lower() == "l":
        if compras:
            for indice, produto  in enumerate(compras):
                print(indice, produto)
        else:
            print("Nada para listar")

    else:
        print("Opção inválida")