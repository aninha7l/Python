conta = int (input("Digite o numero da conta: "))
saldo = float (input("Digite o seu saldo: "))
credito = float (input("Digite o seu credito: "))
debito = float (input("Digite o seu debito: "))
atual = saldo - debito + credito

#saldo atual
print("O seu salario atual e: ", atual)
if atual >=0:

#saldo positivo
 print ("Saldo positivo")
elif atual < 0:

#saldo negativo 
 print ("Saldo negativo")

#saldo igual a 0
else: 
 print ("Saldo igual a zero")
