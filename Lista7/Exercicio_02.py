#usuario digita a quantidade de km percorridos
kmpercorrido = float(input("Digite a quantidade de km percorridos: ")) 
#usuario digita a quantidade de dias pelos quais o carro foi alugado
diasalugados =float(input ("Digite a quantidade de dias pelos quais o carro foi alugado."))
#calculo do preco do carro
precocarro = 120 * diasalugados 
#calculo do preco por km
precokm =  0.15 * kmpercorrido
#calculo do preco final
precofinal= precocarro +precokm
#mostrar ao usuario o preco final
print ("O preço total e:", precofinal)