frase = input("Digite uma frase: ")
caminho_arquivo = "frase.txt"
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(frase)

print(f"Frase salva em {caminho_arquivo}")