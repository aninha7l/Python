base = int(input("Digite a base: "))
expoente =int(input("Digite o expoente: "))
resultado =1

#repete a multiplicacao da base pelo vezes indicado pelo expoente 
for i in range (expoente):

    #multiplica o resultado pela base
    resultado= resultado * base
    print ("Resultado: ", resultado)