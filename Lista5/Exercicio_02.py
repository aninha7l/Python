n1 = float(input("Digite a primeira nota: "))
#solicite a sua primeira nota
n2 = float(input("Digite a segunda nota:"))
#solicite a sua segunda nota
n3= float(input("Digite a terceira nota:"))
#solicite a sua terceira nota

#media do exercicio e media de aproveitamento 
mediaexer = (n1 + n2 + n3 )/3
mediaapro =(n1 + n2 * 2 + n3* 3 + mediaexer) /7

#notaA
if mediaapro >=9:
    print ("Sua nota e A")

#notaB
elif (mediaapro >= 7.5) and (mediaapro < 9):
   print("Sua nota e B")

   #nota C
elif (mediaapro >= 6) and (mediaapro < 7.5):
    print ("Sua nota e C")

    #nota D
elif (mediaapro < 6):
    print("Sua nota e D")