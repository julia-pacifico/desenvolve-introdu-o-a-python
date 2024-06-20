comprimento=int(input("digite o comprimento"))
largura    =int(input("digite a largura"))
preco_m2   =float(input("valoro do m2:"))

area=comprimento*largura #m2
preco_total=area*preco_m2

print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")