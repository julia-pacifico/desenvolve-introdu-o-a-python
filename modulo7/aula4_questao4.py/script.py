import random

def escolher_palavra():
    with open('gabarito_forca.txt', 'r') as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras).lower()

def carregar_enforcado():
    with open('gabarito_enforcado.txt', 'r') as arquivo:
        return arquivo.read().strip().split('\n')

def imprime_enforcado(erros):
    partes_enforcado = carregar_enforcado()
    if erros > len(partes_enforcado) - 1:
        print("Você perdeu! Enforcado completo.")
    else:
        print(partes_enforcado[erros])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas = 6
    letras_utilizadas = set()

    print("Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")
    print("_ " * len(palavra))

    while tentativas > 0:
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").lower()

        if letra in letras_utilizadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_utilizadas.add(letra)

        if letra in palavra:
            letras_corretas.add(letra)
        else:
            tentativas -= 1
            imprime_enforcado(6 - tentativas)
        
        palavra_descoberta = ''.join([letra if letra in letras_corretas else '_ ' for letra in palavra])
        print(palavra_descoberta)

        if all(letra in letras_corretas for letra in palavra):
            print("Parabéns! Você acertou a palavra!")
            break
    
    if tentativas == 0:
        print(f"Você perdeu! A palavra era '{palavra}'.")

jogo_da_forca()