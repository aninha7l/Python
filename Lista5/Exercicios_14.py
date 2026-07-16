cigarrosdia =int(input("Cigarros por Dia"))
anos = int (input("Anos fumando"))


#total de cigarros
totalcigarros = cigarrosdia * 365 *anos 


#minutos perdidos
minutosperdidos = totalcigarros * 10

#dias perdidos 
diasperdidos = minutosperdidos /1440
print("Dias de vida perdidos: "f" {diasperdidos:.2f}") 