caminho_arquivo = 'aula137.txt'

with open(caminho_arquivo, 'w', encoding="utf8") as arquivo:
    arquivo.write("Atenção\n")
    arquivo.write("Linha 2\n")
    arquivo.writelines(
        ("Linha 3\n", "Linha 4\n")
    )