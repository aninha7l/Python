n1 = float(input("Digite o primeiro numero: "))
#solicite o primeiro numero
n2 = float (input("Digite o segundo numero diferente de zero: "))
#solicite o segundo numero diferente de zero

#verificar se o segundo numero e zero
if n2 == 0:

    #Informar que a divisao nao pode ser realizada
    print ("Numero invalido")

    #divisao dos dois numeros 
else:
    divisao = n1 / n2
    print ("A divisao dos numeros e: ", divisao)
    #mostrar a divisao dos numeros