"""
Closure e funções que retornam outras funções
"""
def criar_sadacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

falar_bom_dia = criar_sadacao("Bom dia")
falar_boa_noite = criar_sadacao("Bom noite")


for nome in ["Maria", "joana", "Luiz"]:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))