deposito= float(input("Digite o valor do deposito:"))
taxadejuros =float (input("Digite a taxa de juros:"))
valorinicial =deposito
for mes in range (1,25):
    juros = deposito *(taxadejuros/100)
    deposito = deposito +juros
print(f"mes {mes}:R$ {deposito:.2f}")
jurostotal = deposito - valorinicial
print(f"Valor total de juros:R${jurostotal:.2f}")