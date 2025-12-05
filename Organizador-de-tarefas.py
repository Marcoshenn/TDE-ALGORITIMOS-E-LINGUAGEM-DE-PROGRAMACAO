class Tarefa:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
        self.status = "pendente"

class SistemaTarefas:
    def __init__(self):
        self.tarefas = []
        self.id_atual = 1

    def adicionar_tarefas(self):
        descricao = input("Digite a descrição da tarefa: ")
        tarefa = Tarefa(self.id_atual, descricao)
        self.tarefas.append(tarefa)
        self.id_atual += 1
        print("Tarefa adicionada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
        else:
            for tarefa in self.tarefas:
                print(f"ID:{tarefa.id}, Descrição: {tarefa.descricao}, Status: {tarefa.status}")