# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.60,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostra_argumentos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS:", args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_argumentos_nomeados(1, 2, nome="Joana", qlq=123)
mostra_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    "args1": 1,
    "args2": 2,
    "args3": 3,
    "args4": 4,
}
mostra_argumentos_nomeados(**configuracoes)