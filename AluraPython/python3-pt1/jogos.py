import forca
import advinhacao

def escolher_jogo():
    print("*****************************")
    print("******Escolha seu jogo*******")
    print("*****************************")


    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        forca.jogar()

    elif(jogo == 2):
        print("Jogando advinhação")        
        advinhacao.jogar()

if (__name__ == "__main__"):
    escolher_jogo()