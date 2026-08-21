import importlib

import aula110_m

print(aula110_m.variavel)

for i in range(10):
    importlib.reload(aula110_m)
    print(i)

print("Fim")