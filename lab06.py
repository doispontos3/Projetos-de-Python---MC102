###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Lista de Compras
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

# Leitura de dados
D = float(input())
N = int(input())
pymarket = [] 
bytebazar = [] 
devshop = [] 
pymarket = [float(item) for item in input().split( )]
bytebazar = [float(item) for item in input().split( )]
devshop = [float(item) for item in input().split( )]
matriz = [pymarket, bytebazar, devshop]
# Processamento dos dados
linhas = len(matriz)
colunas = N
produtospymarket = []
produtosbytebazar= []
produtosdevshop = []
receita = True
for produto in range(colunas):
    barateco = matriz[0][produto]
    if matriz[1][produto] < barateco :
            if matriz[2][produto] < matriz[1][produto]:
             barateco = matriz[2][produto]
             D = D - barateco
             if D >= 0 :
                 produtosdevshop.append(produto + 1)
             else:
                 receita = False  
                 D = D + barateco
            else:
             barateco = matriz[1][produto]
             D = D - barateco
             if D >= 0 :
                produtosbytebazar.append(produto + 1)
             else:
                receita = False
                D = D + barateco
    else:
     if matriz[2][produto] < barateco:
        barateco = matriz[2][produto]
        
        D -= barateco
        if D  >= 0 : 
            produtosdevshop.append(produto + 1)
        else:
           receita = False
           D = D + barateco
     else:
        barateco = matriz[0][produto]
        D = D - barateco
        if D >= 0 :
         produtospymarket.append(produto + 1)
        else:
          receita = False
          D = D + barateco
 
# Saída de dados
if  len(produtospymarket ) != 0 :
 print("Itens comprados no PyMarket:")
 print(" ".join(map(str, produtospymarket)))
else:
 print("Nenhum item foi comprado no PyMarket") 

if len(produtosbytebazar) != 0 :
   print("Itens comprados no ByteBazar:")
   print(" ".join(map(str, produtosbytebazar)))
else:
   print("Nenhum item foi comprado no ByteBazar")   

if len(produtosdevshop) != 0 :
   print("Itens comprados no DevShop:")
   print(" ".join(map(str, produtosdevshop)))
else:
   print("Nenhum item foi comprado no DevShop")   

if receita == True :
    print("Foi possível terminar a receita")
else:
   print("Não foi possível terminar a receita")    
