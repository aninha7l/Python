produto  = input ("Digite o nome do produto ")
quantidade = float(input("Quantidade adquirida do produo: "))
preco = float(input("Preco unitario do produto: "))

#preco pago pelo produto
total = quantidade * preco

#desconto a ser aplicado
if quantidade <=5:
    desconto = preco * 0.02
elif (quantidade > 5) and (quantidade <= 10):
    desconto = preco * 0.03
elif quantidade > 10:
    desconto = preco *0.05

    #preco total
    totalpagar = total - desconto
    print ("Total a pagar pelo produto: ", totalpagar)