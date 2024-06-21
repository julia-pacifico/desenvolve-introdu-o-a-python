numero = input("Digite o número: ")

numero = numero.replace(' ', '')

if len(numero) == 8:
    numero_formatado = f"9{numero[:5]}-{numero[5:]}"
elif len(numero) == 9 and numero[0] == '9':
    numero_formatado = f"{numero[:5]}-{numero[5:]}"
else:
    numero_formatado = "Número inválido"

print(f"Número completo: {numero_formatado}")