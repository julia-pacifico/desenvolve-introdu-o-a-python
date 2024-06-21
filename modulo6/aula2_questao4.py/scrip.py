def receber_lista(num):
    tamanho = int(input(f"Digite a quantidade de elementos da lista {num}: "))
    lista = []
    print(f"Digite os {tamanho} elementos da lista {num}:")
    for _ in range(tamanho):
        lista.append(int(input()))
    return lista

lista1 = receber_lista(1)
lista2 = receber_lista(2)

lista_intercalada = []
tamanho_max = max(len(lista1), len(lista2))
for i in range(tamanho_max):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

print("Lista intercalada:", lista_intercalada)