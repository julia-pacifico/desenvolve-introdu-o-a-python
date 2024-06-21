frase = input("Digite uma frase: ")
contador_vogais = 0
indices_vogais = []
vogais = "aeiouAEIOU"

for indice, letra in enumerate(frase):
    if letra in vogais:
        contador_vogais += 1
        indices_vogais.append(indice)

print(f"{contador_vogais} vogais")
print(f"Índices {indices_vogais}")