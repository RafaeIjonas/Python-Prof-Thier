def adicionar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero.")
    return x / y


def principal():
    while True:
        print("Selecione uma opção:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if opcao == 1:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", adicionar(num1, num2))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif opcao == 2:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", subtrair(num1, num2))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif opcao == 3:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", multiplicar(num1, num2))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif opcao == 4:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print("Resultado:", dividir(num1, num2))
            except ValueError as e:
                print(e)

        elif opcao == 5:
            print("Até mais!")
            break

        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    principal()
