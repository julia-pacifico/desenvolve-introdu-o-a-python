def verificar_atributos(classe, forca, magia):
    if classe = "guerreiro":
        return forca >= 15 and magia <= 10
    elif classe = "mago":
        return forca <= 10 and magia >= 15
    elif classe = "arqueiro":
        return 5 < forca <= 15 and 5 < magia <= 15
    else:
        return False

classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

atributos_consistentes = verificar_atributos(classe, forca, magia)

print(f"Pontos de atributo consistentes com a classe escolhida: {atributos_consistentes}")