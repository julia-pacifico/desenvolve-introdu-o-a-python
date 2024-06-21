# Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule 
# a menor quantidade possível de notas necessárias para pagar aquele valor. 
# As notas possíveis são: 100, 50, 20, 10, 5, 2, 1.

quantia = int(input("Digite o valor inteiro: "))

notas100 = quantia // 100
quantia %= 100

notas50 = quantia // 50
quantia %= 50

notas20 = quantia // 20
quantia %= 20

notas10 = quantia // 10
quantia %= 10

notas5 = quantia // 5
quantia %= 5

notas2 = quantia // 2
quantia %= 2

notas1 = quantia // 1
quantia %= 1

print (f"{notas100} nota(s) de R$100,00\n{notas50} nota(s) de R$50,00\n{notas20} nota(s) de R$20,00\n{notas10} nota(s) de R$10,00\n{notas5} nota(s) de R$5,00\n{notas2} nota(s) de R$2,00\n{notas1} nota(s) de R$1,00"