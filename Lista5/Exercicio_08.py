#Inicializa a maior nota com um valor menor que qualquer nota possivel

maior_nota = -1
vencedora =""
#repete o processo paraas 16 candidatas
for i in range(16):
 nome = input(f"Digite o nome da {i+1} ª candidata: ")
nota= float(input(f"Digite a nota de nome {nome}: ")) 

#verifica a maior nota e a vencedora
if nota > maior_nota:
    maior_nota = nota
    vencedora = nome

    print("Vencedora do concurso:", vencedora)
    print("Nota:", maior_nota)

