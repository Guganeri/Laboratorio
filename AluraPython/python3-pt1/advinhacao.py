import random
print("*****************************")
print("Bem-vindo ao jogo de advinhação")
print("*****************************")



numero_secreto = random.randrange(1,101)

while True:    
    chute = int(input("Digite o valor do chute: "))
    if chute == numero_secreto:  
        print("Você acertou !!")  
        print("{}".format(numero_secreto))    
        break
    else:
        if chute > numero_secreto:            
            print("Tente um valor menor")
        elif chute < numero_secreto:
            print("Tente um valor maior")
        
print("FIM")