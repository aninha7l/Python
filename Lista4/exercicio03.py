gasolina = float(input("Digite quanto voce gasta com gasolina: "))
manutencao = float(input("Digite quanto voce gasta em manutencao: "))
IPVA = float (input("Digite quanto voce gasta com IPVA: "))

#media da manutencao do carro
media = (gasolina + manutencao + IPVA)/3
print ("A media de gastos e:", f"{media:.2f}")