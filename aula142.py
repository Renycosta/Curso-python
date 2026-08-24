# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

todo = []

desfeito = []

def listar():
    print("TAREFAS:")
    for i in todo:
        print(i)
    print()

def verificacao_desfazer():
    if todo:
        return desfazer()
    return print("Nada a desfazer\n")

def desfazer():
    des = todo.pop()
    desfeito.append(des)
    listar()

def verificacao_refazer():
    if desfeito:
        return refazer()
    return print("Nada a refazer\n")

def refazer():
    todo.append(desfeito[-1])
    desfeito.pop()
    listar()

def adicionar(tarefa):
    todo.append(tarefa)
    listar()

while True:
    print("Comandos: listar, desfazer, refazer")
    comando_usu  = input("Digite uma tarefa ou comando: ")

    comandos = {
        "listar": lambda: listar(),
        "desfazer": lambda: verificacao_desfazer(),
        "refazer": lambda: verificacao_refazer(),
        "adicionar": lambda: adicionar(comando_usu),
    }

    comando = comandos.get(comando_usu) if comandos.get(comando_usu) is not None else comandos["adicionar"] 
    comando()

    # if comando_usu == "listar":
    #     listar()
    # elif comando_usu == "desfazer":
    #     verificacao_desfazer()
    # elif comando_usu == "refazer":
    #     verificacao_refazer()
    # else:
    #     adicionar(comando_usu)