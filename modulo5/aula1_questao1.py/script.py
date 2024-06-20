n1=float(input("digite o 1º número decimal:"))
n2=float(input("digite o 2º número decimal:"))

diferença_absoluta=abs(n1-n2)
diferença_arredondada= round(diferença_absoluta,2)
print(f"A diferença absoluta entre {n1} e {n2} é {diferença_arredondada}.")