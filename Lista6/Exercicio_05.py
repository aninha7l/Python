#mporta a raiz quadrada da biblioteca -math
from math import sqrt

#cordenadas do primeiro ponto
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1 : "))

#coordenadas do segundo ponto
x2 = float (input("Digite o valor de x2: "))
y2 = float (input("Digite o valor de y2: "))

#calcula a distancia 
distancia = sqrt((x2 - x1) ** 2 + (y2 -y1) **2)
print ("Distancia entre os pontos: "f" {distancia:. 2f}")