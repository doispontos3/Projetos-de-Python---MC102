###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 09 - Álbum de Fotos
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################
import re

# Leitura de dados
n = int(input())
matriz = []
for i in range(n):
    foto = str(input())
    foto = re.split("[,:]", foto)
    foto.pop(0)
    fototratada = []
    for pessoa in foto:
        pessoa = pessoa.strip()
        fototratada.append(pessoa)
    matriz.append(fototratada)
Nomes= []
# Processamento de dados  
for i in range(n):
    for j in range(len(matriz[i])):
        Nomes.append(matriz[i][j])
for i in range(len(Nomes)):
    comparação = Nomes[i]
    for nomes in Nomes:
        if Nomes.index(nomes) != i:
            if nomes == Nomes[i]:
                Nomes.pop(i)
Pessoas = len(Nomes)
quantidade = [] * Pessoas    
for pessoa in Nomes:
    Aparições = 0
    for i in range(n):
        for j in range(len(matriz[i])):
            if matriz[i][j] == pessoa:
                Aparições+= 1
    quantidade.append(Aparições)
qntordenada= []
posições = [i for i in range(Pessoas)]
def maiorindice(quantidade, inicio):
    maior = inicio
    comprimento = len(quantidade)
    for j in range(inicio + 1, comprimento):
        if quantidade[maior] < quantidade[j]:
            maior = j
    return maior
def ordenação(quantidade):
    comprimento = len(quantidade)
    for i in range(comprimento - 1):
        maior = maiorindice(quantidade, i)
        (quantidade[i], quantidade[maior])= (quantidade[maior], quantidade[i])
        (posições[i], posições[maior]) = (posições[maior], posições[i])
    return posições, quantidade
posições, quantidade = ordenação(quantidade)
    
print(quantidade)
print(posições)




# Saída de dados
