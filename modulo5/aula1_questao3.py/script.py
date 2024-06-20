import random 

aleatorio= random.randint(1,10)
acertou=False

while not acertou:
    palpite= int(input("adivinhe o número (entre 1 e 10):"))
    if palpite>aleatorio:
        print("Muito alto, tente novamente!")
    elif palpite<aleatorio:
        print ("muito baixo, tente novamente!")
    else:
        print("parabens! você acertou!")
        acertou=True