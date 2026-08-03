cpf =input("Digite o numero do seu CPF: ")
if len(cpf) !=11 or not cpf.isidigit():
    print("CPF invalido")
elif cpf == cpf[0] * 11:
    print("CPF invalido")
else:
 numeros = [int(d) for d in cpf]
 soma =0
 peso=10
 for numero in numeros[:9]:
        soma += numero * peso
        peso -= 1
        resto = soma %11
 if resto <2:
        digito1 =0
 else:
        digito1 =11 - resto
 soma =0
 peso =11
 for numero in numeros[:9] + [digito1]:
    soma += numero * peso
    peso -= 1
    resto = soma %11
    if resto <2:
        digito2 =0
    else:
        digito2 =11 - resto
    if digito1 == numeros[9] and digito2 == numeros[10]:
        print("CPF valido")
    else:
        print("CPF invalido") 