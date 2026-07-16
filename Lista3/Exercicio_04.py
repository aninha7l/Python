totalEleitores = int (input("Digite o total de eleitores: "))
votob = int (input("Digite o total de votos brancos: "))
voton = int (input("Digite o total de votos nulos : "))
votov= int (input ("Digite o total de votos validos: "))

#porcentagem dos votos
porcentagembrancos = (votob /totalEleitores)*100 
porcentagemnulos = (voton /totalEleitores) *100
porcentagemvalidos = (votov /totalEleitores) * 100
#resultados
print ("Porcentagem de votos brancos : ", porcentagembrancos, "%")
print("Porcentagem de votos nulos :", porcentagemnulos,"%")
print ("Porcentagem de votos validos: ", porcentagemvalidos,"%")
#votos validoos