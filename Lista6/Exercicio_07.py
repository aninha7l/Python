nome = input ("Digite o nome do corretor: ")
quantidade = int ("Digite a quantidade de imoveis vendidos: ")
vendas = float (input("Digite valor total de vendas: "))

#salario base
salario = 2500

#comissao 
comissaoimoveis = (quantidade * 200)
comissaovendas = (vendas * 0.05)

#salario final
salariofinal = salario + comissaoimoveis +comissaovendas

print ("Corretor: ", nome)
print ("Salario final: "f" {salariofinal :.2f}")
