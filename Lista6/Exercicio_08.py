#importa a raiz quadrada da biblioteca math
from math import sqrt

n1 = int(input("Digite um numero positivo:"))
n2  = int (input("Digite outro numero positivo:"))

#calcula o cubo
cubo = n2 ** 3

#media geometrica
mediageo = sqrt (n1 * n2)
#mediageo =sqrt(n1 * n2)
print ("O cubo do segundo numero e: ", cubo)
print ("A media geometrica dos numeros e: ", mediageo)