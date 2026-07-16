morango = float(input("Digite a quantidade de morangos (kg): "))
maca = float(input("Digite a quantidade de macas (kg):"))

#preco morango 
if morango <= 5:
    precomorango = morango * 2.50 
else: 
    precomorango = morango * 2.20

    # preco maca
    if maca <= 5 : 
        precomaca = maca * 1.80
    else:
        precomaca = maca * 1.50

        #valor total da compra 
        total = precomaca + precomorango
        totalkg = maca + morango
        if (totalkg > 8) or (total > 25):
            desconto = total  * 0.10
            total + total - desconto

            print("Valor a pagar: R$", total)
