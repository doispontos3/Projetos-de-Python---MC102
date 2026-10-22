###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Kungsleden
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################


# Leitura de dados
Ns =[int(N) for N in input().split( )]
Floresta = []
for i in range(Ns[0]):
    linha= input().split( )
    Floresta.append(linha)

# Processamento de dados
# cacemos a cabana
for i in range((Ns[0]- 1)):
    for j in range((Ns[1] -1)):
        if Floresta[i][j] == "C":    
            latitude = i
            longitude = j
            break
#agora é as condicionais dos 4 caminhos.
cabanalatitude = latitude + 1
cabanalongitude = longitude + 1

caminho= [Floresta[(latitude)][(longitude)]]
#norte
cabanalatitude-=1
def direção(Floresta, caminho):
    latitude = cabanalatitude
    longitude = cabanalongitude
    caminho.append(Floresta[(latitude-1)][(longitude-1)])
    rota = (len(caminho))
    for i in range(1):
        for j in range((Ns[0])*(Ns[1])):
            try:    
                i = (latitude-1 ) 
                j = (longitude - 1)
                if Floresta[i][j] == "N":
                            latitude-= 1
                            caminho.append(Floresta[(latitude-1)][(longitude-1)])
                if Floresta[i][j] == "S":
                            latitude+= 1
                            caminho.append(Floresta[(latitude-1)][(longitude-1)])
                if Floresta[i][j] == "O":
                            longitude-= 1 
                            caminho.append(Floresta[(latitude-1)][(longitude-1)])
                if Floresta[i][j]== "L":
                            longitude+= 1
                            caminho.append(Floresta[(latitude-1)][(longitude-1)])
# Saída de dados                            
                if Floresta[(latitude-1)][(longitude-1)] == "C":
                     cabana = "cabana"
                     return cabana
                if Floresta[(latitude-1)][(longitude-1)] == "F":
                     saiu = "saiu"
                     return saiu
                rota= (len(caminho))
                if rota > ((Ns[0])*(Ns[1])):
                     girou = "girou"
                     return girou
                if longitude <= 0 or latitude<= 0 or longitude>Ns[1] or latitude>Ns[0]:
                    fugiu = "fugiu"
                    return fugiu
            except IndexError:
                   fugiu = "fugiu"
                   return fugiu                
    return        
caminhonorte = direção(Floresta, caminho)
if caminhonorte == "cabana":
       print("N: de volta a cabana.")
if caminhonorte == "girou":
       print("N: andou em circulos.")
if caminhonorte == "saiu":
       print("N: encontrou o fim da floresta.")
if caminhonorte == "fugiu":
       print("N: caminho sem saida.")
#sul
caminho= [Floresta[(latitude)][(longitude)]]
cabanalatitude+=2
direçãosul= direção(Floresta,caminho)
if direçãosul == "cabana":
       print("S: de volta a cabana.")
if direçãosul == "girou":
       print("S: andou em circulos.")
if direçãosul == "saiu":
       print("S: encontrou o fim da floresta.")
if direçãosul == "fugiu":
       print("S: caminho sem saida.")
#leste
caminho= [Floresta[(latitude)][(longitude)]]
cabanalatitude-=1
cabanalongitude+=1
direçãoleste= direção(Floresta, caminho)
if direçãoleste == "cabana":
       print("L: de volta a cabana.")
if direçãoleste == "girou":
       print("L: andou em circulos.")
if direçãoleste == "saiu":
       print("L: encontrou o fim da floresta.")
if direçãoleste == "fugiu":
       print("L: caminho sem saida.")
#oeste
caminho= [Floresta[(latitude)][(longitude)]]
cabanalongitude-=2
direçãooeste= direção(Floresta, caminho)
if direçãooeste == "cabana":
       print("O: de volta a cabana.")
if direçãooeste == "girou":
       print("O: andou em circulos.")
if direçãooeste == "saiu":
       print("O: encontrou o fim da floresta.")
if direçãooeste == "fugiu":
       print("O: caminho sem saida.")