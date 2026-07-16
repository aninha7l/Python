homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input ("Digite a idade do segundo homem: ")) 
mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int (input("Digite a idade da segunda mulher: "))

#verificacao do maior e menor homem
if homem1 > homem2:
 maiorhomem = homem1
 menorhomem = homem2
else:
 maiorhomem = homem2
 menorhomem = homem1

#verificacao da maior e menor mulher
if mulher1 > mulher2:
    maiormulher = mulher1
    menormulher = mulher2
else:
    maiormulher = mulher2
    menormulher = mulher1
    soma = maiorhomem + menormulher
    produto = menorhomem * maiormulher

    #soma e produto 
    print ("Soma do homem mais velho com a mulher mais nova: ", soma)
    print("produto do homem mais novo com a mulher mais velha: ", produto)