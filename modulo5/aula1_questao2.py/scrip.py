import random
import math

n= int(input("digite a quantidade de valores:"))
soma=0
for i in range(n):
    valor=random.randint(0,100)
    print(valor)
    soma+= valor
print(soma)
print(f"a raiz quadrada dessa soma é {math.sqrt(soma):.2f}")