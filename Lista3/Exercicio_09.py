inicio = float (input("Hora de inicio; "))
fim = float  (input("Hora de termino: "))
#hora do termino do jogo
if fim >= inicio:
      duraçao = fim - inicio 
      print ("A duraçao do jogo foi: ", duraçao, "horas")
else:
      duraçao = (24 - inicio) + fim
      print ("A duracao do jogo foi: " , duraçao, "horas")  
#duracao do jogo