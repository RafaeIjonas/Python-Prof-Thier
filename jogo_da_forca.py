import random

palavras = ['programacao', 'trabalho',
            'desenvolvimento', 'tecnologia', 'professores']


def escolher_palavra():
    return random.choice(palavras)


def exibir_forca(tentativas):
    if tentativas == 0:
        print("  O")
    elif tentativas == 1:
        print("  O")
        print(" /|\\")
    elif tentativas == 2:
        print("  O")
        print(" /|\\")
        print(" /")
    elif tentativas == 3:
        print("  O")
        print(" /|\\")
        print(" / \\")
    else:
        print("  X")
        print(" /|\\")
        print(" / \\")


def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 6
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca Da Estácio, que comece os jogos HA HA HA!")
    print("_ " * len(palavra_oculta))
    print("\n")

    while tentativas > 0 and '_' in palavra_oculta:
        letra = input("Por favor, digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
        else:
            letras_tentadas.append(letra)

            if letra in palavra:
                for i, letra_palavra in enumerate(palavra):
                    if letra_palavra == letra:
                        palavra_oculta[i] = letra
            else:
                tentativas -= 1
                print("Essa letra não está na palavra.")

        exibir_forca(tentativas)
        print(" ".join(palavra_oculta))
        print("\n")

    if '_' not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra.")
    else:
        print("Você perdeu! A palavra correta era {}.".format(palavra))

    print("Obrigado por jogar! Até a Próxima!")


if __name__ == "__main__":
    jogar()
