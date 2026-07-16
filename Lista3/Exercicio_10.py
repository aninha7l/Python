hora = float (input("Horas trabalhadas:"))
valor = float (input("Valor por hora :"))
semana =4
if (hora <= 40) and (hora >= 0):
    salario = (valor * hora * semana)
    print ("O salario do funcionario e: ",salario)
elif hora > 40:
    extra = (valor * hora * semana)
    salario = (extra * hora * semana)
   # salario com extra 
elif hora > 40:
    extra = (valor * 0.5)
    salario = (extra * hora * semana)
    print ("O salario do funcionario com o extra e: ", salario)