def valida_cpf(cpf):
    cpf = ''.join(c for c in cpf if c.isdigit())
    if len(set(cpf)) == 1:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_1 = 0
    else:
        digito_verif_1 = 11 - resto
    if digito_verif_1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_2 = 0
    else:
        digito_verif_2 = 11 - resto
    if digito_verif_2 != int(cpf[10]):
        return False

    return True
cpf = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")

if valida_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")