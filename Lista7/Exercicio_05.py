casa =float(input("Digite o valor da casa:"))
salario = float (input("Digite o valor do salario:"))
anos = int (input("Digite a quantidade de anos a pagar:"))
meses = anos * 12
prestacao = casa/meses
if prestacao > (salario *0.30):
    print("Emprestimo negado")
else:
    print("Emprestimo aprovado")