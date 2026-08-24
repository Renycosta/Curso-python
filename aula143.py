# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json


def listar():
    print("TAREFAS:")
    dados_todo = ler()
    for i in dados_todo:
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
    tarefa = tarefa.strip()
    todo.append(tarefa)
    listar()

def ler(tarefas):
    dados_todo = []
    try:
        with open("aula143_todo.json", "r", encoding="utf-8") as arquivo:
            dados_todo = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não existe")
        salvar(tarefas)
    return dados_todo

def salvar(comando_usu):
    with open("aula143_todo.json", "w", encoding="utf-8") as arquivo:
        json.dump(comando_usu, arquivo, ensure_ascii=False)

todo = ler([])

desfeito = []

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
    salvar(todo)