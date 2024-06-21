import random
def encrypt(nome, chave):
    nome_criptografado = []
    for letra in nome:
        codigo = ord(letra) + chave
        if codigo > 126:
            codigo -= 94
        nome_criptografado.append(chr(codigo))
    return ''.join(nome_criptografado)

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave_aleatoria = random.randint(1, 10)
nomes_criptografados = [encrypt(nome, chave_aleatoria) for nome in nomes]

print(f"Nomes criptografados: {nomes_criptografados}")
print(f"Chave utilizada: {chave_aleatoria}")