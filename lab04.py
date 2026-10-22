###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Chefe de Cozinha
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

# Leitura da entrada

horainicial = 18 * 60
horafinal = 23 * 60
horaatual = horainicial
pedidosatendido = 0

# Processamento dos dados

while True:
 horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]
 horadopedido = horas * 60 + minutos
 if(horadopedido >= horainicial and horadopedido < horafinal):
  if((horas + minutos) == 0):
   break
  if(horadopedido >= horaatual):
   horaatual = tempo_pedido + horadopedido
   pedidosatendido += 1
  else:
   horaatual += tempo_pedido
   pedidosatendido += 1
 else:
  print("oxe ta chapano")
 if(horaatual >= horafinal):
  break 

# Saída de dados
print(pedidosatendido - 1)
