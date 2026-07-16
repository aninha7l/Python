peso = float(input("Digite seu peso: "))
#Solicitou peso do usuario
altura = float(input("Digite sua altura:"))
#Solicitou a altura do usuario

imc = (peso) /(altura ** 2)
# Se imc for maior que 18.5 e considerado abaixo do peso
if imc < 18.5:
     print("Abaixo do peso")

if imc >= 18.5 and imc < 25:
 # Se imc for  maior que 18.5 e maior que  25 e considerado peso normal
     print("Peso normal")

# Se o imc for maior que 25 e menor que  30 e considerado sobrepeso
     if imc >= 25 and imc < 30:
          print("Sobrepeso")

# Se o imc for maior e igual a 30 ou menor que 35 e considerado obeso
          if imc >= 30 and imc < 35:
               print("Obeso")

# Se o imc for maior que 35 e considerado obesidade morbida
               if imc >= 35:
                    print("Obesidade morbida")
#mostrar a obesidade morbida