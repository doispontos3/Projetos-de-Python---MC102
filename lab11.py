###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - No Man's Sky
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

PROTOTIPOS = ('PD', 'PA', 'PTR', 'PTE', 'PC', 'PR', 'PO', 'PV')
PAISAGENS = ('SOA', 'SVM', 'SCO', 'SF1', 'SF2', 'SF3', 'SL', 'SPC')
CONDICOES_CLIMATICAS = ('CC0', 'CC1', 'CC2', 'CN1', 'CN2', 'CN3', 'CN4', 'CV', 'CTA1', 'CTA2', 'CTE1')

TERRENO_PROTO = {
  'PD':  ('TD', 'TA2'),
  'PA':  ('TA1 TA2', 'TD TP TM'),
  'PTR': ('TP TM', 'TAR TO1 TO2'),
  'PTE': ('TP TM', 'TAR TO1 TO2 TC'),
  'PC':  ('TC TM', 'TO1 TO2 TP'),
  'PR':  ('TC TM', 'TO1 TO2'),
  'PO':  ('TO1 TO2', 'TAR TM'),
  'PV':  ('TM', 'TP TC')
}

TERRENO_ADJACENCIA = {
  'TAR': 'TAR TO1 TP TC TM',
  'TO1': 'TAR TO1 TO2 TM',
  'TO2': 'TO1 TO2',
  'TA1': 'TA1 TA2 TP TC TM',
  'TA2': 'TA1 TA2 TD TC TM',
  'TD': 'TA2 TD',
  'TP': 'TAR TA1 TA2 TP TC TM',
  'TC': 'TAR TA1 TA2 TP TC TM',
  'TM': 'TAR TO1 TA1 TA2 TP TC TM'
}

ELEMENTOS = {
  # Scenarios
  'SOA' : ('PA',               'TA1 TA2'),
  'SVM' : ('PTR PTE PR PO',    'TO1 TO2'),
  'SCO' : ('PTR PTE PR PO',    'TO1'),
  'SF1' : ('PTR PTE',          'TP TM'),
  'SF2' : ('PTR PTE',          'TP TM'),
  'SF3' : ('PA PTR PTE',       'TP TM'),
  'SL'  : ('PTR PTE',          'TP TM TC'),
  'SPC' : (PROTOTIPOS,         'TC TM'),
  # Weather conditions
  'CC0' : ('PTR PTE PC PR PO', 'TAR TO1 TO2 TP TC TM'),
  'CC1' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CC2' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CN1' : ('PTE PR PO',        'TAR TP TC TM'),
  'CN2' : ('PTE PC PR PO',     'TAR TP TC TM'),
  'CN3' : ('PTE PC',           'TAR TP TC TM'),
  'CN4' : ('PC',               'TAR TP TC TM'),
  'CV'  : ('PV',               'TP TC TM'),
  'CTA1': ('PD PA',            'TD'),
  'CTA2': ('PD PA PV',         'TD TA2 CV'),
  'CTE1': ('PR',               'TM TO1 TO2'),
  # Animals
  'AMA' : (PROTOTIPOS,         'TD TA2'),
  'AAV' : (PROTOTIPOS,         'TAR TP TA1 TC TM'),
  'AMM' : (PROTOTIPOS,         'TO1 TO2 TAR'),
  'APE' : (PROTOTIPOS,         'TO1 TO2 SL TAR'),
  'AAL' : (PROTOTIPOS,         'TAR TP SL TO1'),
  'ACR' : (PROTOTIPOS,         'TAR TO1'),
  'AHQ' : (PROTOTIPOS,         'TAR TA1 TP TM'),
  'ARO' : (PROTOTIPOS,         'TAR TA1 TA2 TD TC TM'),
  'AFE' : (PROTOTIPOS,         'TAR TA1 TP TC TM SF1'),
  'ACA1': (PROTOTIPOS,         'TP TC TM SF1'),
  'ACA2': (PROTOTIPOS,         'TP TC TM SF1'),
  'AHOT': (PROTOTIPOS,         'TP TC TM SF1 SF2 SF3')
}

# Leitura de dados
planetatipo = input()
Ns =[int(N) for N in input().split( )]
mundo = []* (Ns[1]-1)
for i in range((Ns[0])):
  linha= input().split(",")
  mundo.append(linha)
for i in range((len(PROTOTIPOS))):
  if planetatipo == PROTOTIPOS[i]:
    listaalfa= TERRENO_PROTO[PROTOTIPOS[i]]
list4= []
for treco in listaalfa:
  list4.append(treco.split( ))
lista=[]
for i in list4:
  for j in i:
    lista.append(j)

  

  
# Processamento de dados
#Regra 1
verificaçãoprototipo = []
for i in range((len(mundo))):
    pa = (len(mundo[i]))
    linha0 = []
    for j in range((pa)):
      linha0.append(mundo[i][j].split( ))
    verificaçãoprototipo.append(linha0)
#Saída de dados
terrenosinvalido= []
latitude= []
longitude= []
regra1= True
for lenha in verificaçãoprototipo:
  for coluna in lenha:
      for terreno in coluna:
        if terreno[0] == "T":
          if terreno not in lista:
            regra1= False
            latitude.append(verificaçãoprototipo.index(lenha))
            longitude.append((lenha.index(coluna)+1))
            terrenosinvalido.append(terreno)
print("regra 1")
if regra1 == True:
  print("ok")
else:
  for i in range((len(terrenosinvalido))):
    print('{0},{1}:{2}'.format(latitude[i],longitude[i],terrenosinvalido[i]))
  print("falha")

#Regra 2
regra2 = True
latitude = []
longitude = []
terrenosinvalido = []
terrenos = []
for linhaa in verificaçãoprototipo:
  linha=[]
  for colunaa in linhaa:
    coluna= []
    for terreno in colunaa:
      if terreno[0]== "T":
        coluna.append(terreno)
    if coluna:
      linha.append(coluna)    
  terrenos.append(linha)
#versao com colunas vazia
latitude = []
longitude = []
setores = []
for linhaa in verificaçãoprototipo:
  linha=[]
  for colunaa in linhaa:
    coluna= []
    for terreno in colunaa:
      if terreno[0]== "T":
        coluna.append(terreno)
    linha.append(coluna)    
  setores.append(linha)
semcolunas = []
for linhaa in terrenos:
  linha=[]
  for coluna in linhaa:
      for terreno in coluna:
        linha.append(terreno)
  semcolunas.append(linha)
for i in range(len(terrenos)):
  j= -1
  for terreno in semcolunas[i]:
    j+=1
    try:
              if semcolunas[(i-1)][j] not in TERRENO_ADJACENCIA[terreno]:
               if latitude and longitude:
                 if i != latitude[-1] or j != longitude[-1]:
                  regra2 = False
                  if (i-1) <= -1:
                    latitude.append((len(terrenos)-1))
                  else:  
                    latitude.append((i))
                  longitude.append((j))
                  terrenosinvalido.append(terreno)
               else:
                 regra2 = False
                 if (i-1) <= -1:
                    latitude.append((len(terrenos)-1))
                 else:  
                    latitude.append((i))
                 longitude.append((j))
                 terrenosinvalido.append(terreno)
                
    except IndexError:
          break
    try:
           if semcolunas[i][(j-1)] not in TERRENO_ADJACENCIA[terreno]:
             if latitude and longitude:
              if i != latitude[-1] or j != longitude[-1]:
                regra2 = False
                latitude.append((i))
                longitude.append((j))
                terrenosinvalido.append(terreno)
             else:
               regra2 = False
               if (i-1) <= -1:
                    latitude.append((len(terrenos)-1))
               else:  
                    latitude.append((i))
               longitude.append((j))
               terrenosinvalido.append(terreno)   
    except IndexError:
          break
    try:
           if semcolunas[(i+1)][j] not in TERRENO_ADJACENCIA[terreno]:
             if latitude and longitude:
              if i != latitude[-1] or j != longitude[-1]:
                regra2 = False
                latitude.append(i)
                longitude.append((j))
                terrenosinvalido.append(terreno)
             else:
              regra2 = False
              if (i-1) <= -1:
                  latitude.append((len(terrenos)-1))
              else:  
                  latitude.append((i))
              longitude.append((j))
              terrenosinvalido.append(terreno)
          
    except IndexError:
          if semcolunas[0][j] not in TERRENO_ADJACENCIA[terreno]:
            if i != latitude[-1] or j != longitude[-1]:
                regra2 = False
                latitude.append((i))
                longitude.append((j))
                terrenosinvalido.append(terreno)
                
    try:
          if semcolunas[i][(j+1)] not in TERRENO_ADJACENCIA[terreno]:
             if latitude and longitude:
              if i != latitude[-1] or j != longitude[-1]:
                regra2 = False
                latitude.append(i)
                longitude.append((j))
                terrenosinvalido.append(terreno)
             else:
               regra2 = False
               if (i-1) <= -1:
                 latitude.append((len(terrenos)-1))
               else:  
                 latitude.append((i))
               longitude.append((j))
               terrenosinvalido.append(terreno)
          
    except IndexError:
          if semcolunas[i][0] not in TERRENO_ADJACENCIA[terreno]:
            if latitude and longitude:
              if i != latitude[-1] or j != longitude[-1]:
                regra2 = False
                latitude.append((i))
                longitude.append((j))
                terrenosinvalido.append(terreno)
            else:
               regra2 = False
               if (i-1) <= -1:
                    latitude.append((len(terrenos)-1))
               else:  
                    latitude.append((i))
               longitude.append((j))
               terrenosinvalido.append(terreno)
               
#agr é caçar o setor dos terreno
#a latitude nos da as linha e longitude as posição na linha
#primeiro vamo remover os repetidos
for i in range(len(latitude)):
   for h in range(len(latitude)):
      try:
        if h != i:
          if latitude[i] == latitude[h] and longitude[i]==longitude[h] and terrenosinvalido[i]==terrenosinvalido[h]:
            latitude.pop(h)
            longitude.pop(h)
            terrenosinvalido.pop(h)
      except IndexError:
         break
setorlongitude = []
for i in range(len(latitude)):
   aux= longitude[i]
   contador = 0
   j = 0
   for coluna in setores[latitude[i]]:
       if contador < aux:
        j+=1
        for terreno in coluna:
          contador +=1
          if contador >= aux:
              setorlongitude.append(j)    
       else:
         break
print("regra 2")
if regra2 == True:
  print("ok")
else:
  for i in range((len(terrenosinvalido))):
    print('{0},{1}:{2}'.format(latitude[i],longitude[i],terrenosinvalido[i]))
  print("falha")
#Regra 3
#agr verificar evendtos e coisas. S = paisagem, C = clima e A= animais. 
#paisagem, condições e fauna
#vamos utilizar a matriz setores com os terrenos e verificaçãoprototipos. na real só a segunda ja da bom. 
# #ele usa as mema coordenadas da matriz semcolunas
semcolunas = []
for linhaa in verificaçãoprototipo:
  linha=[]
  for coluna in linhaa:
      for terreno in coluna:
        linha.append(terreno)
  semcolunas.append(linha)
regra3= True
latitude= []
longitude = []
terrenosinvalido= []
for linha in semcolunas:
   for coisa in linha:
      if coisa[0]!="T":
        if planetatipo not in ELEMENTOS[coisa][0]:
           regra3= False
for i in range(len(semcolunas)):
  colunaterreno = -1
  for j in range(len(semcolunas[i])):
    if semcolunas[i][j][0]=="T":
      colunaterreno+=1
      try:
        if semcolunas[i][j+1][0] !="T":  
            if semcolunas[i][j] in ELEMENTOS[semcolunas[i][j+1]][1]:
              g=0
              while semcolunas[i][((j+1)+g)][0]!="T":
                g+=1
              terrenor= [semcolunas[i][j]]
              fauna= []
              paisagem=[]
              clima=[]
              for k in range(1, (g+1)):
                if semcolunas[i][j+k][0]=="C":
                  clima.append(semcolunas[i][j+k])
                if semcolunas[i][j+k][0]=="S":
                  paisagem.append(semcolunas[i][j+k])
                if semcolunas[i][j+k][0]=="A":
                  fauna.append(semcolunas[i][j+k])
              if paisagem:
                for h in range(len(paisagem)):
                  if semcolunas[i][j] not in ELEMENTOS[paisagem[h]][1]:
                        if latitude and longitude:
                          if latitude[-1]!= i or longitude[-1]!= colunaterreno: 
                            regra3= False
                            latitude.append(i)
                            longitude.append(colunaterreno)
                            terrenosinvalido.append(semcolunas[i][j])
                            break
                        else:
                          regra3= False
                          latitude.append(i)
                          longitude.append(colunaterreno)  
                          terrenosinvalido.append(semcolunas[i][j])
                          break
              if clima: 
                for h in range(len(clima)):
                  if "CV" in clima and "CTA2" in clima:
                     clima.remove("CTA2")
                  for f in range(len(terrenor)):  
                    if terrenor[f] not in ELEMENTOS[clima[h]][1]:
                        if latitude and longitude:
                          if latitude[-1]!= i or longitude[-1]!= colunaterreno: 
                            regra3= False
                            latitude.append(i)
                            longitude.append(colunaterreno)
                            terrenosinvalido.append(semcolunas[i][j])
                            break
                        else:
                          regra3= False
                          latitude.append(i)
                          longitude.append(colunaterreno)  
                          terrenosinvalido.append(semcolunas[i][j])
                          break    
                if fauna:  
                  for h in range(len(fauna)):
                    if semcolunas[i][j] not in ELEMENTOS[fauna[h]][1]:
                        if latitude and longitude:
                          if latitude[-1]!= i or longitude[-1]!= colunaterreno: 
                            regra3= False
                            latitude.append(i)
                            longitude.append(colunaterreno)
                            terrenosinvalido.append(semcolunas[i][j])
                            break
                        else:
                          regra3= False
                          latitude.append(i)
                          longitude.append(colunaterreno)  
                          terrenosinvalido.append(semcolunas[i][j])
                          break
                    for f in range(len(paisagem)):    
                      if paisagem[f] not in ELEMENTOS[fauna[h]][1]:
                          if latitude and longitude:
                            if latitude[-1]!= i or longitude[-1]!= colunaterreno: 
                              regra3= False
                              latitude.append(i)
                              longitude.append(colunaterreno)
                              terrenosinvalido.append(semcolunas[i][j])
                              break
                          else:
                            regra3= False
                            latitude.append(i)
                            longitude.append(colunaterreno)  
                            terrenosinvalido.append(semcolunas[i][j])
                            break
                                        
            else:      
              regra3= False
              latitude.append(i)
              longitude.append(colunaterreno)
              terrenosinvalido.append(semcolunas[i][j])
      except IndexError:
         break        
       
print("regra 3")
if regra3 == True:
  print("ok")
else:
  for i in range((len(terrenosinvalido))):
    print('{0},{1}:{2}'.format(latitude[i],longitude[i],terrenosinvalido[i]))
  print("falha")                  
           
#comparaçoes a se fazer: 
# terrenos nas paisagens, terrenos nos climas, climas nos climas, terrenos nos animais, paisagens nos animais