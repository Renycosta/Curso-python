# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def mostrar_perguntas(dicionario):
    quantidade_corretas = 0

    for pergunta in dicionario:
        print(f"Pergunta: {pergunta["Pergunta"]}\n")

        print("Opções:")
        mostrar_opcoes(pergunta["Opções"])

        resposta_usuario = input("Escolha uma opção: ")

        quantidade_corretas += corrigir(resposta_usuario, pergunta["Opções"], pergunta["Resposta"])

    print(f"Você acertou {quantidade_corretas} de {len(dicionario)} perguntas")

def mostrar_opcoes(opcoes):
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")
    print()

def corrigir(resposta_usuario, opcoes, resposta):
    if resposta_usuario.isdigit():
        resposta_usuario_int = int(resposta_usuario)

    if resposta_usuario_int is not None:
        if resposta_usuario_int >= 0 and resposta_usuario_int < len(opcoes):
            if opcoes[resposta_usuario_int] == resposta:
                acertou = True

    if acertou:
        print("Acertou\n")
        return 1
    print("Errou\n")
    return 0

mostrar_perguntas(perguntas)