###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Dependências de Tarefas II
# Nome: Felipe de Freitas Percinoto
# RA: 275170
###################################################

"""
Função para detectar ciclos nas dependências das tarefas,
que deve ser implementada de forma recursiva.

Argumentos:
    - dependências: matriz com as dependências de cada tarefa
    - tarefa: tarefa sendo analisada
    - visitadas: lista de tarefas que já foram analisadas
Retorno:
    Essa função deve retornar True se não houver ciclos nas
    dependências da tarefa e False caso contrário.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
"""
def verifica_tarefas(dependencias, tarefa, visitadas):
    if len(visitadas)>= len(dependencias):
        return True
    tarefa= dependencias[len(visitadas)]
    if tarefa[0] == 0:
        tarefas_possiveis= True
        if len(visitadas)< len(dependencias):
            visitadas.append(tarefa)
            if len(visitadas)>= len(dependencias):
                return tarefas_possiveis
            return verifica_tarefas(dependencias, tarefa, visitadas)
        else:
            return tarefas_possiveis       
    for i in tarefa:
        if (len(visitadas)+1) in dependencias[(i-1)]:
            tarefas_possiveis = False
            return tarefas_possiveis
    visitadas.append(tarefa)
    return verifica_tarefas(dependencias, tarefa, visitadas)
# Leitura de dados
N = int(input())
dependencias = []
for i in range(N):
    tarefa = [int(N) for N in input().split( )]
    dependencias.append(tarefa)
# Verificação das dependências entre as tarefas
i= 0
tarefa= dependencias[i]
visitadas= []

tarefas_possiveis= verifica_tarefas(dependencias, tarefa, visitadas)

# Impressão da saída
if tarefas_possiveis:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma tarefa não pode ser realizada")