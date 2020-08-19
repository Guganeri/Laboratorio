print("*****************************")
print("Bem-vindo ao jogo de advinhação")
print("*****************************")

numero_secreto = 52

while True:    
    chute = int(input("Digite o valor do chute: "))
    if chute == numero_secreto:        
        break
    else:
        print("tente novamente")
        
print("FIM")