#entrada
idade= int(input("digite sua idade"))
ja_jogou=input("já jogou pelo menos 3 jogos de tabuleiro?")
quantidade=int(input("quantos jogos ja venceu?"))

#processamento
ingresso= (idade <= 18) and (idade>= 16) and (ja_jogou) and (quantidade>=1)

apto=ingresso

print(f"apto para ingressar no clube de jogos de tabuleiro:{ingresso}")