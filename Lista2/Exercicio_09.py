idade = int (input ("Digite a sua idade: "))
# de 0 a 3 anos e considerado bebe
if idade >= 0 and idade < 3:
    print ("Bebe")

elif idade >=3 and idade < 13:
    print ("Criança")
# de 3 a 13 anos e considerado crianca

elif idade >= 13 and idade < 18:
    print ("Adolescente")
    # de 13 a 18 anos e considerado adolescente
elif  idade >= 18 and idade < 65:
    print ("Adulto")
    # de 18 a 65 e considerado adulto
else:
    print ("Idoso")
# idoso