tipos = input("Digite o tipo de combustivel (A - alcool,  G - gasolina,):").upper()
litros= float (input("Digite a quantidade de litros: "))

#combustivel escolhido: A
if tipos =="A":
    preco = 3.90
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

        #combustivel escolhido: G
        if tipos == "G":
            preco = 6.30
            if litros <= 20:
                desconto = 0.04
        else:
            desconto =0.06
        valortotal = litros * preco * (1 - desconto)
        print ("Valor a pagar: "f" {valortotal:.2f}") 
       

