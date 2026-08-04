#pede o deposito inicial
deposito = float(input("Deposito inicial: " ))
#pede a taxa de juros e o deposito mensal
taxa =float(input("Taxa de juros: "))
#pede o deposito mensal
depositomensal =float(input("Deposito mensal: "))
valorinicial = deposito
for mes in range (1,25):
    #calcula os juros
    juros = deposito * (taxa/100)
    #calcula o deposito mensal
    deposito = deposito + juros
    print(f"mes {mes}: R$ {deposito:.2f}")
    jurostotal = deposito - valorinicial -(depositomensal *24)
    print(f"Valor total de juros: R$ {jurostotal:.2f}")
print(f"Valorfinal do acumulado: R$ {deposito:.2f}")