###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Geladeiras Subzero
# Nome:
# RA:
###################################################

# leitura de dados
tipo = str(input())
pessoas = int(input())
potencia = int(input())


# Verificação e impressão do nome do modelo a ser recomendado
if(tipo == "S"):
 if(pessoas <= 2):
  if(potencia <= 70):
   print("Gel-S")
  elif(potencia <= 130): 
   print("Gel-SPlus")
  else:
   print("Frost++") 
 elif(pessoas == 3):
  if(potencia <= 130):
   print("DeluxFF") 
  else:
   print("Frost++")
 elif(pessoas >= 4):
  if(potencia <= 100):  
   print("IceCold")
  elif(potencia <= 130):
   print("DeluxFF")
  else:
   print("Frost++")
else:
 if(pessoas == 1):
  print("Gel-D")
 elif(pessoas == 2):
  if(potencia <= 150):
   print("Gel-DPlus")
  else:
   print("DupCold")
 elif(pessoas == 3):
  if(potencia <= 100):
   print("Gel-DPlus")
  else:
   print("DupCold")
 else:
  if(potencia <= 100):
   print("IceCold")          
  else:
   print("Frost++")
