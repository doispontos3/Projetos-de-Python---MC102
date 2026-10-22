###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - O Caso do Medalhão Roubado 
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

# Leitura da entrada
N = int(input())

museu = []
for _ in range(N):
    museu.append(list(input()))

M = int(input())
suspeitos = {}
for _ in range(M):
    letra, pistas = input().split( )
    suspeitos[letra] = pistas.split(",")

# Verificação da posição do detetive
for i in range(N):
    for j in range(len(museu[i])):
        if museu[i][j] == "D":    
            detetive= (i,j)
            break
       
# Coleta das pistas
caminhofeito= [detetive]
caminhoaseandar= [detetive]
# definiremos a caminhada pela matriz como fariamos em um plano cartesiano com vetores unitarios pras quatro direções
# nao sei pq n ensinaram conjuntos, sao ate que chave pra n repetir nem fudendo
#salvaremos tudo em formato de coordenadas
def catartreco(museu, caminhofeito):
    direçãos= [(1,0),(-1,0),(0,1),(0,-1)]
    while caminhoaseandar:
        x,y= caminhoaseandar[0]
        caminhoaseandar.pop(0)
        for vetor in direçãos:
            i,j = vetor
            flinston, blenins= (x+i),(y+j)
            if 0<= flinston < len(museu) and 0<=blenins< len(museu[0]) and (flinston,blenins) not in caminhofeito:
                if museu[flinston][blenins]!= "#":
                    caminhofeito.append(((flinston),(blenins)))                
                    caminhoaseandar.append(((flinston),(blenins)))
    return caminhofeito
caminhofeito = list(catartreco(museu,caminhofeito))
pistasencontrada= []
for lugar in caminhofeito:
    x,y = lugar
    if museu[x][y]!= "." and museu[x][y]!= "D":
        pistasencontrada.append(museu[x][y])
        
               
# Verificação dos suspeitos e impressão da saída
desgraçados=[]
quantidade=[]
for pista in pistasencontrada:
    for suspeito in suspeitos:
        if pista in suspeitos[suspeito]:
            desgraçados.append(suspeito)
unicos= []
for suspeito in desgraçados:
    if suspeito not in unicos:
        unicos.append(suspeito)
for suspeito in unicos:
    vezes= 0
    for suspeito2 in desgraçados:
        if suspeito == suspeito2:
            vezes+=1
    quantidade.append(vezes)


#tem que fazer contagem de quem mais aparece
inicio=0
def maiorindiceqnt(quantidade, inicio):
      maior = inicio
      comprimento = len(quantidade)
      for j in range(inicio + 1, comprimento):
          if quantidade[maior] < quantidade[j]:
              maior = j
      return maior
def ordenacaoqnt(quantidade):
      comprimento = len(quantidade)
      for i in range(comprimento - 1):
          maior = maiorindiceqnt(quantidade, i)
          (quantidade[i], quantidade[maior])= (quantidade[maior], quantidade[i])
          (unicos[i], unicos[maior]) = (unicos[maior], unicos[i])
      return unicos, quantidade
unicos, quantidade = ordenacaoqnt(quantidade)

inicio = 0
fudido=[]
i= 0
fudido.append(unicos[i])
if len(quantidade)>1:
    while quantidade[i]==quantidade[i+1]:
        i+=1
        fudido.append(unicos[i])
        if (i+1)>(len(quantidade)-1):
            break
def maiorindice(quantidade, inicio):
      maior = inicio
      comprimento = len(quantidade)
      for j in range(inicio + 1, comprimento):
          if quantidade[maior] > quantidade[j]:
              maior = j
      return maior
def ordenação(quantidade):
      comprimento = len(quantidade)
      for i in range(comprimento - 1):
          maior = maiorindice(quantidade, i)
          (quantidade[i], quantidade[maior])= (quantidade[maior], quantidade[i])
      return quantidade
fudido = ordenação(fudido)
print(*fudido)


        
    