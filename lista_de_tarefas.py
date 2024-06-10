import tkinter as tk


class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tarefas")
        self.tasks = []

        # Criar elementos da interface
        self.task_label = tk.Label(master, text="Tarefa:")
        self.task_label.pack()

        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(
            master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(master)
        self.tasks_listbox.pack()

        self.remove_button = tk.Button(
            master, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.update_tasks_listbox()
        self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            task_index = self.tasks_listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.update_tasks_listbox()
        except:
            print("Selecione uma tarefa para remover")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)


root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
