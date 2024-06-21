from collections import Counter

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
frase = ''.join(e for e in frase if e.isalnum())
contador_objetivo = Counter(palavra_objetivo.lower())
anagramas = []

for palavra in frase.split():
    if len(palavra) == len(palavra_objetivo):
        contador_palavra = Counter(palavra.lower())
        if contador_palavra == contador_objetivo:
            anagramas.append(palavra)

print(f"Anagramas: {anagramas}")