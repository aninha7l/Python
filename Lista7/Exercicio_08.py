#Pede o deposito inicial
deposito= float(input("Digite o valor do deposito:"))
#Pede a taxa de juros
taxadejuros =float (input("Digite a taxa de juros:"))
valorinicial =deposito
for mes in range (1,25):
    #calcula o valor do juros do mes
    juros = deposito *(taxadejuros/100)
    deposito = deposito +juros
print(f"mes {mes}:R$ {deposito:.2f}")
jurostotal = deposito - valorinicial
#mostrar o valor total de juros
print(f"Valor total de juros:R${jurostotal:.2f}")