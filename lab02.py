###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Escolhendo seu Cartão de Crédito
# Nome:
# RA:
###################################################

# Leitura da entrada
x= int(input())
y= int(input())
z= float(input())
k= int(input())
# Cálculos e impressão da saída
if(((12 * k) - x + (12 * k * z / 100) + (y * 12)) <= (12 * k)):
 print("True")
else:
 print("False")