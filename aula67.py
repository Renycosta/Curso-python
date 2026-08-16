"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re
import sys

# cpf = ("746.824.890-70").replace(".", "").replace("-", "")
cpf = re.sub(
    r'[^0-9]',
    "",
    "746.824.890-70"
)

entrada_e_sequencial = cpf == cpf[0] * len(cpf)
if entrada_e_sequencial:
    print("Você enviou dados sequenciais")
    sys.exit()

# 1° Digito
cpf_corrigido1 = cpf[:9]

contagem_regressiva1 = 10
soma_resultados1 = 0

for digito in cpf_corrigido1:
    valores_multiplicados = contagem_regressiva1 * int(digito)
    soma_resultados1 += valores_multiplicados
    contagem_regressiva1 -= 1

conta1 = (soma_resultados1 * 10) % 11
primeiro_digito = conta1 if conta1 <= 9 else 0

print(f"1° Digito:{primeiro_digito}")

# 2° Digito
cpf_corrigido2 = cpf_corrigido1 + str(primeiro_digito)

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
cpf_gerado_pelo_calculo = f"{cpf_corrigido1}{primeiro_digito}{segundo_digito}"

if cpf == cpf_gerado_pelo_calculo:
    print(f"{cpf} é válido")
else:
    print("CPF inválido")