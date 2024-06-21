import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []
    for palavra in palavras:
        if len(palavra) > 3:  
            inicio = palavra[0]
            fim = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = ''.join([inicio] + meio + [fim])
            resultado.append(palavra_embaralhada)
        else:
            resultado.append(palavra)
    return ' '.join(resultado)
