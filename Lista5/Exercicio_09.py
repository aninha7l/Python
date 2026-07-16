numero = int(input("Digite um numero: "))

divisores = 0

#percorre todos os numeros de 1 ate o numero informado
for i in range (1, numero +1):

    #verificar se i e um divisor do numero
    if numero % i == 0:
        print(i)
        divisores += 1
        
        #verifica se o numero e primo
        if divisores ==2:
         print("O numero e primo.")
         if divisores ==2:
            print("O numero e primo")
         else:
            print("O numero nao e primo")
