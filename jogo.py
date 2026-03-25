import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("=== Jogo de Adivinhação ===")
    print(f"Tente adivinhar o número entre 1 e 100. Você tem {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        try:
            chute = int(input("\nDigite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if chute < numero_secreto:
            print(f"Muito baixo! Tentativas restantes: {max_tentativas - tentativas}")
        elif chute > numero_secreto:
            print(f"Muito alto! Tentativas restantes: {max_tentativas - tentativas}")
        else:
            print(f"\n Parabéns! Você acertou em {tentativas} tentativa(s)!")
            return

    print(f"\n Você perdeu! O número era {numero_secreto}.")

jogo_adivinhacao()
