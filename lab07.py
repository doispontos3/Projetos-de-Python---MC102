###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Dependências de Tarefas I
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

# Leitura de dados
tarefas_possiveis = True
tarefas = [int(tarefa) for tarefa in input().split( )]
dependencia = []
tarefa = []
ultimoadc = (-1)
posição= 1

# Verificação das dependências entre as tarefas
for i in range(len(tarefas)):
    i = (tarefas[posição] - 1)
    posição = i
    if tarefas[posição] != posição + 1 :      
         ultimoadc += 1
         i = (tarefas[posição] - 1)
         tarefa.append(posição + 1)
         dependencia.append(tarefas[posição])
         if ultimoadc > 0:
             if tarefa[0] == dependencia[ultimoadc]:
                tarefas_possiveis = False
             elif tarefa[(ultimoadc - 1)] == dependencia[ultimoadc]:
                 tarefas_possiveis= False

    
    # para o tabela do futuro, veja sobre recursão pra poder continuar sem usar o segundo for problematico#





# Impressão da saída
if tarefas_possiveis == True:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma das tarefas não pode ser realizada")