salariofixo = float (input("Salario fixo: "))
carro = int (input("Numero de carro vendidos: ")) 
vendas = float (input("Valor total das vendas: "))

#comissao
comissaocarro =float (input("Valor da  comissao por carro vendido: "))
comissao =(carro * comissaocarro) + (vendas * 0.05)

#comissao
salarioFinal = salariofixo + comissao

#resultado do salario final
print ("O salario final e: ", salarioFinal)


