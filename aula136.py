caminho_arquivo = 'aula136.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.writelines(
        ("Linha 3\n", "Linha 4\n")
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print("READLINE")
    arquivo.seek(0, 0)
    print(arquivo.readline(), end="")
    print(arquivo.readline().strip())
    print("READLINES")
    for linha in arquivo.readlines():
        print(linha.strip())

print("-" * 20)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())