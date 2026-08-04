#usuario informa a velocidade do carro em km/h
velocidade = float(input("Escreva a velocidade do carro em km/h:"))
#se a velocidade for maior que 80km/h, o usuario sera multado em R$50,00
if velocidade >80:
 excesso = velocidade -80
 #excesso de velocidade multiplicacao por R$50,00 para calcular o valor da multa
 multa = 50 * excesso
 print("Voce foi multada. O valor da multa é: R$" f"{multa:.2f}")
 #senao, o usuario nao sera multado
else:
     print("Voce nao foi multada")

