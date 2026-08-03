deposito = float(input("Deposito inicial: " ))
taxa =float(input("Taxa de juros: "))
depositomensal =float(input("Deposito mensal: "))
valorinicial = deposito
for mes in range (1,25):
    juros = deposito * (taxa/100)
    deposito = deposito + juros
    print(f"mes {mes}: R$ {deposito:.2f}")
    jurostotal = deposito - valorinicial -(depositomensal *24)
    print(f"Valor total de juros: R$ {jurostotal:.2f}")
print(f"Valorfinal do acumulado: R$ {deposito:.2f}")