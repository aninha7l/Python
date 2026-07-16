codigo = int(input("Digite o seu codigo : "))
#solicite seu codigo
nascimento = int (input("Digite o ano do seu nascimento: "))
#solicite o ano do seu nascimento
ingresso = int(input("Digite o ano do seu ingresso na empressa:"))
#solicite o ano do seu ingresso na empressa

#calcular a idade do funcionario
idade = 2026 - nascimento

#calcular o tempo na empressa
tempo = 2026 - ingresso
print ("Sua idade e: ", idade, "anos")
print ("Seu tempo na empressa e: ", tempo,"anos") 

#requer aposentadoria 
if ((idade >= 65 ) and (tempo >= 25)or (idade >= 60)and (tempo >= 30)):
    print("requerer_aposentadoria")

    #nao requerer aposentadoria 
else:
    print("Nao requerer")
