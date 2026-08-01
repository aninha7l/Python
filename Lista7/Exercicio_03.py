velocidade = float(input("Escreva a velocidade do carro em km/h:"))
if velocidade >80:
 excesso = velocidade -80
 multa = 50 * excesso
 print("Voce foi multada. O valor da multa é: R$" f"{multa:.2f}")
else:
     print("Voce nao foi multada")

