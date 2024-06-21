import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)
maior_qtd_negativos = []
inicio_intervalo = 0
for i in range(len(lista)):
    if lista[i] < 0:
        if not maior_qtd_negativos or len(maior_qtd_negativos) < len(lista[inicio_intervalo:i+1]):
            maior_qtd_negativos = lista[inicio_intervalo:i+1]
    else:
        inicio_intervalo = i + 1

if maior_qtd_negativos:
    lista = [num for num in lista if num not in maior_qtd_negativos]

print("Editada: ", lista)