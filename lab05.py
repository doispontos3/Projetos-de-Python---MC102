###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Tit for Tat
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

# Leitura da entrada
jogada_inimiga = 0
ponto_inimigo = 0
ponto_nosso = 0
jogada_anterior = 0
# Processamento dos dados
k= int(input())
for i in range(0, k):
 jogada_inimiga = int(input())
 if jogada_anterior == 0:
    nossa_play = 0
    if jogada_inimiga == 0:
        ponto_nosso += 3
        ponto_inimigo += 3
        print(nossa_play)
    else:
       ponto_nosso = ponto_nosso
       ponto_inimigo += 5
       print(nossa_play)
 else:
    nossa_play = 1          
    if jogada_inimiga == 0:
        ponto_nosso += 5
        ponto_inimigo = ponto_inimigo
        print(nossa_play)
    else:
       ponto_nosso += 1
       ponto_inimigo += 1
       print(nossa_play)
 jogada_anterior = jogada_inimiga

# Saída de dados
print(ponto_nosso)
print(ponto_inimigo)