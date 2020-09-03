print("*****************************")
print("******Escolha seu jogo*******")
print("*****************************")


import forca
import advinhacao

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    forca.jogar()

elif(jogo == 2):
    print("Jogando advinhação")
    advinhacao.jogar()