print("*****************************")
print("Bem-vindo ao jogo de advinhação")
print("*****************************")

numero_secreto = 52

while True:    
    chute = int(input("Digite o valor do chute: "))
    if chute == numero_secreto:  
        print("Você acertou !!")      
        break
    else:
        if chute > numero_secreto:            
            print("Tente um valor menor")
        elif chute < numero_secreto:
            print("Tente um valor maior")
        
print("FIM")