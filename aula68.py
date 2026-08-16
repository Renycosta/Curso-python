import random

nove_digitos = ""
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contagem_regressiva1 = 10
soma_resultados1 = 0

for digito in nove_digitos:
    valores_multiplicados = contagem_regressiva1 * int(digito)
    soma_resultados1 += valores_multiplicados
    contagem_regressiva1 -= 1

conta1 = (soma_resultados1 * 10) % 11
primeiro_digito = conta1 if conta1 <= 9 else 0

print(f"1° Digito:{primeiro_digito}")

# 2° Digito
cpf_corrigido2 = nove_digitos + str(primeiro_digito)

contagem_regressiva2 = 11
soma_resultados2 = 0

for digito in cpf_corrigido2:
    valores_multiplicados = contagem_regressiva2 * int(digito)
    soma_resultados2 += valores_multiplicados
    contagem_regressiva2 -= 1

conta2 = (soma_resultados2 * 10) % 11
segundo_digito = conta2 if conta2 <= 9 else 0

print(f"2° Digito:{segundo_digito}")

# Confirmação cpf
cpf_gerado_pelo_calculo = f"{nove_digitos}{primeiro_digito}{segundo_digito}"

print(cpf_gerado_pelo_calculo)