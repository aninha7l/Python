#usuario informa a distancia percorrida em km
distancia = float(input("Digite a distancia percorrida em km :"))
#se a distancia for menor ou igual a 200km, o preco da passagem sera de R$0,50 por km
if distancia <=200:
    #calcule o preco da passagem multiplicando a distancia por R$0,50
    preco = distancia * 0.50
    print(" O preco da passagem e: R$ "f"{preco:.2f}")
else: 
    preco = distancia * 0.45
    print(" O preco da passagem e: R$ "f"{preco:.2f}")