l1= int(input ("Digite o primeiro lado: "))
l2 = int(input ("Digite o segundo lado"))
l3 = int (input ("Digite o terceiro lado"))
if l1 + l2 <= l3 or l1 + l3 <= 12 or l2 +l3 <= l1:
    print ("Nao e possivel formar um triangulo com esses lados")
elif l1 == l2 == l3:
    #Nao e possivel formar um triangulo com tres lados 
    print ("O triangulo e equilatero")
#equilatero
elif l1== l2 or l1 == l3 or l2 == l3:
   print ("O triangulo e isosceles")
#isosceles
else:
    print("O triangulo e escaleno")
#escaleno