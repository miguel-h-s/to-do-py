tarefas = []

def menu():
    print("\n1 - adicionar tarefa")
    print("2 - ver tarefas")
    print("0 - sair")

def adicionar():
    nome = input("nome da tarefa: ")
    tarefas.append(nome)
    print(f"tarefa '{nome}' adicionada!")

def ver():
    if not tarefas:
        print("nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i} - {tarefa}")

print("bem vindo a To-Do List!")

while True:
    menu()

    escolha = int(input("escolha: "))

    if escolha == 0:
        print("saindo...")
        break

    elif escolha == 1:
        adicionar()

    elif escolha == 2:
        ver()

    else:
        print("opção inválida")
