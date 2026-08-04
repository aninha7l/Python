 #usuario informa a quantidade de kwh consumidos e o tipo de instalacao
kwh = int(input("Digite a quantidade de kwh consumidos:"))
tipo = str(input("Digite o tipo de instalacao (R, I ou C):")).upper()
 #se o tipo escolhido for R
if tipo == "R" and kwh <= 500:
  preco = 0.40
elif kwh > 500:
  preco = 0.65
  #se o tipo escolhido for I
if tipo == "I" and kwh <= 1000:
  preco = 0.55
elif kwh > 1000: 
  preco = 0.60
  #se o tipo escolhido for C
if tipo == "C" and kwh <= 5000:
  preco = 0.55
elif kwh > 5000:
  preco = 0.60
preco_total = kwh * (kwh + preco)
print("Preço total a se pagar: R$" f"{preco_total:.2f}")