soma = 0

#percorre todos os numeros de 2 ate 100
for numero in range(2, 101):

    #considere inicialmente que o numero e primo
    primo =True 

    for i in range(2, numero):

        #verifica se a divisao temresto zero
        #se tiver, significa que o numero nao e primo
        if numero % i == 0:

            #indica que o numero nao e primo
            primo = False
            break

        #soma os numeros primo de 1 a 100
        if primo:
            soma = soma + numero

            print("soma dos primos = ", soma)