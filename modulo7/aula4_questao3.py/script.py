import os
import re

caminho_arquivo = os.path.join(os.getcwd(), "estomago.txt")

codcs = ['utf-8', 'latin-1', 'iso-8859-1']

primeiras_25_linhas = []
linha_mais_longa = ""
numero_linhas = 0
contagem_nonato = 0
contagem_iria = 0

for codec in codcs:
    try:
        with open(caminho_arquivo, 'r', encoding=codec) as arquivo:
            linhas = arquivo.readlines()
            
            primeiras_25_linhas = linhas[:25]
            
            numero_linhas = len(linhas)
            
            linha_mais_longa = max(linhas, key=len).strip()
            
            for linha in linhas:
                contagem_nonato += len(re.findall(r'\bNonato\b', linha, flags=re.IGNORECASE))
                contagem_iria += len(re.findall(r'\bÍria\b', linha, flags=re.IGNORECASE))

        break
    
    except UnicodeDecodeError:
        continue

print("Texto das primeiras 25 linhas:")
for linha in primeiras_25_linhas:
    print(linha.strip())

print("\nNúmero total de linhas:", numero_linhas)
print("\nLinha com maior número de caracteres:")
print(linha_mais_longa)
print("\nNúmero de menções aos nomes 'Nonato' e 'Íria':")
print("Nonato:", contagem_nonato)
print("Íria:", contagem_iria)