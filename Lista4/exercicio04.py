time1 = input ("Digite o nome do primeiro time: ")
gols1 = (input("Gols do primeiro time: "))
time2 = input ("Digite o nome do segundo time: ")
gols2 = int (input("Gols do segundo time:"))

#time 1 vencedor
if gols1 > gols2:
    print ("Vencedor: ", time1)

    #time 2 vencedor
elif gols2 > gols1:
    print ("Vencedor:", time2)
    #empate
else:
    print ("Empate!")
