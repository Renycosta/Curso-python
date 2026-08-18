# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return multiplicador * num
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(1))
print(triplicar(1))
print(quadruplicar(1))