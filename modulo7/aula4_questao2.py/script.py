import string
frase = input("Digite uma frase: ")
caminho_arquivo = "frase.txt"
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(frase)

print(f"Frase salva em {caminho_arquivo}")

caminho_arquivo_frase = "frase.txt"
with open(caminho_arquivo_frase, 'r') as arquivo:
    frase = arquivo.read()

frase_limpa = ''.join(caracter for caracter in frase if caracter.isalpha() or caracter == ' ')

palavras = frase_limpa.split()
palavras_formatadas = '\n'.join(palavras)

caminho_arquivo_palavras = "palavras.txt"
with open(caminho_arquivo_palavras, 'w') as arquivo:
    arquivo.write(palavras_formatadas)

print(f"Conteúdo do arquivo {caminho_arquivo_palavras}:")
print(palavras_formatadas)