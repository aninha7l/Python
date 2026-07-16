acima5 = 0
div3 = 0
print ("Numeros sorteados: ")

for i in range (1, 21):
    import random

    #sorteia os numeros de 1 a 20
    num = random.randintin(1, 20)
    print (num)

    #verifica quantos numeros sao maiores que 5
    if num > 5:
        acima5 = acima5 +1

        #verifica quantos numeros sao divisiveis por 3
        if (num % 3 ==0):
            div3 = div3 + 1
            print ("Quantidade de numeros acima de 5: ", acima5)
            print ("Quantidade de numeros divisiveis por 3: ", div3)
