#entrada
nome= input("Digite o nome de usuário:")

preco_total = 0

produto1= input("Digite o nome do produto 1:")
preço1= float(input("Digite o preço unitário do produto 1:"))
quantidade1= int(input("Digite a quantidade do produto 1:"))
preco_total +=preço1*quantidade1

produto2= input("Digite o nome do produto 2:")
preço2= float(input("Digite o preço unitário do produto 2:"))
quantidade2= int(input("Digite a quantidade do produto 2:"))
preco_total +=preço2*quantidade2

produto3= input("Digite o nome do produto 3:")
preço3= float(input("Digite o preço unitário do produto 3:"))
quantidade3= int(input("Digite a quantidade do produto 3:"))
preco_total +=preço3*quantidade3




#saida
print(f"total: R$ {preco_total:,.2f}")