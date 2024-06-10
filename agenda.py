class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("Contato já existe.")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print("Nome: {}, Telefone: {}".format(nome, self.contatos[nome]))
        else:
            print("Contato não encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print("Nome: {}, Telefone: {}".format(nome, telefone))


def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Pesquisar contato")
        print("4. Listar contatos")
        print("5. Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if opcao == 1:
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == 2:
            nome = input("Digite o nome do contato: ")
            agenda.remover_contato(nome)
        elif opcao == 3:
            nome = input("Digite o nome do contato: ")
            agenda.pesquisar_contato(nome)
        elif opcao == 4:
            agenda.listar_contatos()
        elif opcao == 5:
            print("Até mais!")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    menu()
