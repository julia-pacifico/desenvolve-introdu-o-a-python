import string
def limpar_texto(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    texto = texto.replace(' ', '')
    return texto
def eh_palindromo(frase):
    texto_limpo = limpar_texto(frase)
    return texto_limpo == texto_limpo[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')