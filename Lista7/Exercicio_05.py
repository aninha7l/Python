#usuario informa o valor da casa,salario e a quantidade de anos a pagar
casa =float(input("Digite o valor da casa:"))
salario = float (input("Digite o valor do salario:"))
anos = int (input("Digite a quantidade de anos a pagar:"))
meses = anos * 12
prestacao = casa/meses
#se a prestacao for maior que 30% do salario,o emprestimo sera negado
if prestacao > (salario *0.30):
    print("Emprestimo negado")
    #senao,o emprestimo sera aprovado
else:
    print("Emprestimo aprovado")