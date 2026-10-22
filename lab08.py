###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Processamento de Dados
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################
import re

# Leitura de dados
n = int(input())
naocapitalise= ["de", "dos", "do","da","das", "e"]
for i in range(n):
    Nome = str(input()).split( )
    data = str(input())
    data = re.sub("[/,-]", "",data)
    endereço = str(input())
    endereço = re.split("[ - ,]", endereço)
    endereço.pop(-2)
    telefone = str(input())
    telefone = re.sub("[()-]", "", telefone)
    nenome = []
    neendefeçoc = []
# Processamento de dados
    for nome in Nome:
        nome = str.lower(nome)
        if nome not in naocapitalise:
             nenome.append(nome.capitalize())
        else: 
            minusculo1 = str.lower(nome)
            nenome.append(minusculo1)
    for endereco in endereço:
        endereco= str.lower(endereco)
        if endereco not in naocapitalise:
            neendefeçoc.append(endereco.capitalize())
        else:
            minusculo = str. lower(endereco)
            neendefeçoc.append(minusculo)
        neendefeçocnovo = [endereco for endereco in neendefeçoc if endereco != " " and "-"]    
    neendefeçocnovo[-2] = neendefeçocnovo[-2] + ","
    
    
    

# Saída de dados
    print(*nenome)
    print("{0}{1}-{2}{3}-{4}{5}{6}{7}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
    print(*neendefeçocnovo)
    print("({0}{1}){2}{3}{4}{5}{6}-{7}{8}{9}{10}".format(telefone[0],telefone[1],telefone[2],telefone[3],telefone[4],telefone[5],telefone[6],telefone[7],telefone[8],telefone[9],telefone[10]))
