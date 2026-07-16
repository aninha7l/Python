#peca ao usuario o valor da mercadoria
preco = float(input("Digite o valor da mercadoria:"))
#peca o usuario o valor do percentual em desconto
desconto_p = float(input("Digite o valor de percentual do desconto_p: "))
        
        #desconto
desconto = desconto_p/100

        #mostrar o valor do desconto 
print("O valor do desconto e : ", desconto)

        #do preco final
preco_final = preco - (preco * desconto)

    # mostrar ao usuario o preco finally
print("Preco final da mercadoria: ", preco_final)