chopps = int(input("Quantidade de chopps: "))
coberturas = int(input("Quantidade de coberturas da pizza: "))
pessoas = int(input("Quantidade de pessoas: "))

#quantidade total de chopps
totalchopps = chopps * 5

#valor total da pizza 
totalpizza = 50 + (coberturas * 2.5)

totalconta = totalchopps + totalpizza 

#taxa
taxa = totalconta * 0.10

#valor total da conta
totalconta = totalconta +taxa

#valor que cada pessoa paga 
porpessoa = totalconta /pessoas
print ("Total da conta com 10%: R$ "f"{totalconta:.f}")
print (" Cada pessoa paga: R$ " f" {porpessoa:.2f}")


