lista = []
while len(lista) < 4:
    num = int(input("Digite um número inteiro: "))
    lista.append(num)

print("Lista original:", lista)
print("Os 3 primeiros elementos:", lista[:3])
print("Os 2 últimos elementos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Elementos de índice par:", lista[::2])
print("Elementos de índice ímpar:", lista[1::2])