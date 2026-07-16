quantidadeAtual = int (input("Digite a quantidade atual do estoque: "))
maxima = int (input("Digite a quantidade maxima do estoque: "))
minima = int (input("Digite a quantidade minima do estoque: "))

#calculo da media do estoque
media = (maxima + minima)/2
if quantidadeAtual >= media:
    print ("Nao efetuar compra")
else:
    print ("Efetuar compra")