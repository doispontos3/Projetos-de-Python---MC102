###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Jogos Olímpicos
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

# Leitura da quantidade de provas e pesos
N, O, P, B = [int(i) for i in input().split()]

# Leitura das provas
olimpiada= []
for i in range(N):
    entrada= input().split("-")
    prova= []
    for coisa in entrada:
        prova.append(coisa.strip())
    olimpiada.append(prova)
olimpiada= tuple(olimpiada)
podiosro=[]
for fuleco in olimpiada:
    fuleco = tuple(fuleco)
    prova= list(fuleco)
    prova.pop(0)
    prova.pop(0)
    podiosro.append(prova)
podios=[]
for podio in podiosro:
    prova=[]
    for item in podio:
        if item != "RO":
            prova.append(item)
    podios.append(prova)
países=[]
for podio in podios:
    for pais in podio:
        if pais not in países:
            países.append(pais)
países= tuple(países)
medalhas=[]
for pais in países:
    medalhapais=[0,0,0]
    for podio in podios:
        for colocado in podio:
            if pais == colocado:
                if podio.index(colocado) == 0:
                    medalhapais[0]+=1
                if podio.index(colocado) == 1:
                    medalhapais[1]+=1
                if podio.index(colocado) == 2:
                    medalhapais[2]+=1
    medalhas.append(medalhapais)
medalhas= tuple(medalhas)
medalhasro=[]
for pais in países:
    medalhapaisro=[0,0,0,0]
    for podio in podiosro:
        for colocado in podio:
            if pais == colocado and colocado!="RO":
                if podio.index(colocado) == 0:
                    medalhapaisro[1]+=1
                    if "RO" in podio:
                        medalhapaisro[0]+=1
                if podio.index(colocado) == 1:
                    medalhapaisro[2]+=1
                if podio.index(colocado) == 2:
                    medalhapaisro[3]+=1
    medalhasro.append(medalhapaisro)
# Ordenação pelo Critério Oficial
y=0
def maiorindiceouro(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
            if x[maior][0] < x[j][0]:
                maior = j
    return maior
def maiorindiceprata(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if x[maior][0]==x[j][0]:
            if x[maior][1] < x[j][1]:
                maior = j              
    return maior
def maiorindicebronze(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if x[maior][0]==x[j][0]:
            if x[maior][1]==x[j][1]:
                if x[maior][2] < x[j][2]:
                    maior = j
    return maior
def menorindiceletra(x,y,medalhasco):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if medalhasco[maior][0]==medalhasco[j][0]:
            if medalhasco[maior][1]==medalhasco[j][1]:
                if medalhasco[maior][2] == medalhasco[j][2]:
                    if x[maior] > x[j]:
                        maior = j
    return maior
def ordenação(x,maiorindice,países):
    comprimento = len(x)
    for i in range(comprimento-1):
        maior = maiorindice(x, i)
        (x[i], x[maior])= (x[maior], x[i])
        (países[i], países[maior]) = (países[maior], países[i])
    return países, x
def ordenaçãoum(x,maiorindice,medalhasco):
    comprimento = len(x)
    for i in range(comprimento-1):
        maior = maiorindice(x,i,medalhasco)
        (x[i], x[maior])= (x[maior], x[i])     
    return x
paísesco= list(países)
medalhasco= list(medalhas)
paísesco, medalhasco= ordenação(medalhasco,maiorindiceouro,paísesco)
paísesco, medalhasco= ordenação(medalhasco,maiorindiceprata,paísesco)
paísesco, medalhasco= ordenação(medalhasco,maiorindicebronze,paísesco)
paísesco = ordenaçãoum(paísesco,menorindiceletra,medalhasco) 
print('Critério Oficial:')
print(" - ".join(paísesco))


# Ordenação Ponderado
paísesponderado= list(países)
medalhasponderado= list(medalhas)
y=0
def ponderado(medalhas,O,P,B):
    pesos= []
    for medalha in medalhas:
        pesos.append((O*medalha[0]+P*medalha[1]+B*medalha[2]))
    return pesos
def maiorindice(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
            if x[maior] < x[j]:
                maior = j
    return maior
def menorindiceletrapon(x,y,pesos):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if pesos[maior]==pesos[j]:
            if x[maior] > x[j]:
                maior = j
    return maior
pesos= ponderado(medalhasponderado,O,P,B)
paísesponderado, pesos= ordenação(pesos,maiorindice,paísesponderado)
paísesponderado =ordenaçãoum(paísesponderado,menorindiceletrapon,pesos)  
print('Ponderado:')
print(' - '.join(paísesponderado))

# Ordenação por Recordes Olímpicos
y=0
def maiorindicerecorde(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
            if x[maior][0] < x[j][0]:
                maior = j
    return maior
def maiorindiceouro(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if x[maior][0]==x[j][0]:
            if x[maior][1] < x[j][1]:
                maior = j              
    return maior
def maiorindiceprata(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if x[maior][0]==x[j][0]:
            if x[maior][1]==x[j][1]:
                if x[maior][2] < x[j][2]:
                    maior = j
    return maior
def maiorindicebronze(x,y):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if x[maior][0]==x[j][0]:
            if x[maior][1]==x[j][1]:
                if x[maior][2] == x[j][2]:
                    if x[maior][3] < x[j][3]:
                        maior = j
    return maior
def menorindiceletraro(x,y,medalhasco):
    maior = y
    comprimento = len(x)
    for j in range(y + 1, comprimento):
        if medalhasco[maior][0]==medalhasco[j][0]:
            if medalhasco[maior][1]==medalhasco[j][1]:
                if medalhasco[maior][2] == medalhasco[j][2]:
                    if medalhasco[maior][3]== medalhasco[j][3]:
                        if x[maior] > x[j]:
                            maior = j
    return maior
paísesro= list(países)
paísesro, medalhasro= ordenação(medalhasro,maiorindicerecorde,paísesro)
paísesro, medalhasro= ordenação(medalhasro,maiorindiceouro,paísesro)
paísesro, medalhasro= ordenação(medalhasro,maiorindiceprata,paísesro)
paísesro, medalhasro = ordenação(medalhasro,maiorindicebronze,paísesro)
paísesro = ordenaçãoum(paísesro,menorindiceletraro,medalhasro)
print('Recorde Olímpico:')
print(" - ".join(paísesro))
# Ordenação por Dobradinha
podiosdo=[]
for prova in olimpiada:
    prova.pop(1)
    podiosdo.append(prova)
medalhasdo=[]
for pais in países:
    medalhapaisdo=[0,0,0,0]
    for podio in podiosdo:
        try:
            for j in range(len(podiosdo)):
                if j!=podiosdo.index(podio):
                    if podio[0] == podiosdo[j][0]:
                        if podio[1] == podiosdo[j][1]==pais:
                            medalhapaisdo[0]+=1
            for colocado in podio:
                if pais == colocado and colocado in países:
                    if podio.index(colocado) == 1:
                        medalhapaisdo[1]+=1
                    if podio.index(colocado) == 2:
                        medalhapaisdo[2]+=1
                    if podio.index(colocado) == 3:
                        medalhapaisdo[3]+=1
        except IndexError:
            for colocado in podio:
                if pais == colocado and colocado in países:
                    if podio.index(colocado) == 1:
                        medalhapaisdo[1]+=1
                    if podio.index(colocado) == 2:
                        medalhapaisdo[2]+=1
                    if podio.index(colocado) == 3:
                        medalhapaisdo[3]+=1

    medalhasdo.append(medalhapaisdo)
paísesdo= list(países)
paísesdo, medalhasdo= ordenação(medalhasdo,maiorindicerecorde,paísesdo)
paísesdo, medalhasdo= ordenação(medalhasdo,maiorindiceouro,paísesdo)
paísesdo, medalhasdo= ordenação(medalhasdo,maiorindiceprata,paísesdo)
paísesdo, medalhasdo = ordenação(medalhasdo,maiorindicebronze,paísesdo)
paísesdo = ordenaçãoum(paísesdo,menorindiceletraro,medalhasdo)
print('Dobradinha:')
print(' - '.join(paísesdo))