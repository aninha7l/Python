maça = float (input("Digite a quantidade de maças compradas:"))
if maça <12:
    preço = maça * 1.30
    print ("O preço total e: ",preço)
elif maça >= 12:
    preço = maça  * 1.00
    print ("O preço total e : ", preço)
    #preço total de maça compradas