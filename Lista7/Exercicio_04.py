distancia = float(input("Digite a distancia percorrida em km :"))
if distancia <=200:
    preco = distancia * 0.50
    print(" O preco da passagem e: R$ "f"{preco:.2f}")
else: 
    preco = distancia * 0.45
    print(" O preco da passagem e: R$ "f"{preco:.2f}")