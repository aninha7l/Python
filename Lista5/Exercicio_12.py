ap =75
diariaNormal =292

#calcula a diaria promocional com 25% de desconto
diariaPromo = diariaNormal - (diariaNormal * 0.25)

#calcula o valor total arrecadado com 80% de ocupacao e diaria promocional
arrec80 =(ap * 0.80) * diariaPromo

#calcula valor total arrecadado com 50% de ocupacao e diaria normal
arrec50 = (ap * 0.50) * diariaNormal

#calcula a diferenca entre esses dois valored
diferenca = arrec80 - arrec50
print("Diaria normal: R$ ", diariaNormal)
print ("Diaria promocional: R$ " f" {diariaPromo:.2f}")
print ("Arrecadacao com 80%:R$ "f"{arrec80:.2f}")
print ("Arrecadacao com 50%: R$ " f"{arrec50:.2f}")
print ("Diferenca: R$ " f"{diferenca:.2f}")