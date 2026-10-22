###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Labirinto de Creta
# Nome: 
# RA: 
###################################################

'''
Função para simular o caminho percorrido pelo Teseu, essa função deve ser
implementada de forma recursiva. A função recebe a matriz representando o
mapa, a posição (i,j) do Teseu, a energia E de Teseu, a energia G de um
gigante e a energia M do Minotauro. A função deve retornar se Teseu
conseguiu derrotar o Minotauro.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
'''
def caminho(mapa, i, j, E, G, M,visitados):
    '''Primeiro vai ser feito as comparações de uma posição atual e logo em seguida será feito as 
    análises atrás de uma nova posição. O plano é, a cada posição com múltiplas escolhas tomado,Teseu
    volte a essa posição, exclua o caminho 'ruim' e tente outro caminho.'''
    direçãos= [(1,0),(-1,0),(0,1),(0,-1)]
    if visitados is None:
        visitados=[]
    if mapa[i][j]=='.':
        E-=1
    if mapa[i][j]=='G':
        E-=G
    if mapa[i][j]=='M':
        E-=M
    if mapa[i][j]=="M" and E>=0:#caso base aqui
        return True
    visitados.append((i,j))
    for x,y in direçãos:
        u,v= i+x,j+y
        if len(mapa)>u>=0 and len(mapa[0])>v>=0  and (u,v) not in visitados:
            if mapa[u][v]!="#" and E>0:
                if caminho(mapa, u, v, E, G, M,visitados): #função se chama nesse if
                    return True
    visitados.remove((i,j))               
    return False

# . . .

# Leitura da entrada
N, E, G, M = [int(i) for i in input().split()]
i, j = [int(i) for i in input().split()]

mapa = []
for _ in range(N):
  mapa.append(input().split())

# Simulação do jogo
Teseu = caminho(mapa, i, j, E, G, M,visitados= None)

# Impressão da saída
if Teseu:
    print("Teseu derrotou o Minotauro")
else:
    print("Teseu não derrotou o Minotauro")