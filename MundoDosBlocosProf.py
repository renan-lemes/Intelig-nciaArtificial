''' 
    Nome: Renan Lemes Leepkaln
    Curso: Matemática Aplicada e Computacional
    Mundo Dos blocos.
'''

import random
import sys


""" 
   
    Primeiro sempre ta na base 
    [A , B, C] = 
    
    [C]
    [B]
    [A]
    [[A,B,C], [],[]] ok
    [[C,B,A], [], []] ok
    [[C,A,B], [], []] ok 
    [[B,A,C], [], []] ok
    [[B,C,A],[],[]]  ok
    [[A,C,B],[],[]] ok
    o algoritmo é em profundidade

"""

letraA = 'A'
letraB = 'B'
letraC = 'C'


EstadoFinal = [letraA, letraB, letraC]
Listaesq = []
Listameio = []
Listadir = []
flag = 0

Listadir = random.sample(EstadoFinal, 3)

#Listadir = [letraB, letraC, letraA]

ConjLista = [Listadir, Listameio, Listaesq]

def MostrarListas(ConjLista, flag):
    print('Movimentos feitos', flag)
    print('---------------------------')
    print(ConjLista[0], ConjLista[1], ConjLista[2])
    print('---------------------------')

MostrarListas(ConjLista, flag)

def FimDeJogo(ConjLista, flag):
    if(ConjLista[0] == EstadoFinal):
        MostrarListas(ConjLista, flag)
        print('Fim de jogo !!!!')
        sys.exit()
    if(ConjLista[1] == EstadoFinal):
        MostrarListas(ConjLista, flag)
        print('Fim de jogo !!!!')
        sys.exit()
    if(ConjLista[2] == EstadoFinal):
        MostrarListas(ConjLista, flag)
        print('Fim de jogo !!!!')
        sys.exit()

def Desempilha(ConjLista, flag):
    ''' 
        Função destinada para fazer o desenpilhamento das listas
        Essa função está okay
    '''
    if(len(ConjLista[1]) == 0 and len(ConjLista[2]) == 0):
        FimDeJogo(ConjLista, flag)
        Listameio.append(Listadir[2])
        Listadir.remove(Listadir[2])
        flag += 1
        MostrarListas(ConjLista, flag)
        Listaesq.append(Listadir[1])
        Listadir.remove(Listadir[1])
        flag +=1
        MostrarListas(ConjLista, flag)

    if(len(ConjLista[0]) == 0 and len(ConjLista[2]) == 0):
        FimDeJogo(ConjLista, flag)
        Listadir.append(Listameio[2])
        Listameio.remove(Listameio[2])
        flag+=1
        MostrarListas(ConjLista, flag)
        Listaesq.append(Listameio[1])
        Listameio.remove(Listameio[1])
        flag+=1
        #aux = Listameio[0]
        #Listameio[0] = Listadir[0]
        #Listadir[0] = aux
        MostrarListas(ConjLista, flag)
    if(len(ConjLista[0]) == 0 and len(ConjLista[1]) == 0):
        FimDeJogo(ConjLista, flag)
        Listameio.append(Listaesq[2])
        Listaesq.remove(Listaesq[2])
        flag+=1
        MostrarListas(ConjLista, flag)
        Listadir.append(Listaesq[1])
        Listaesq.remove(Listaesq[1])
        flag+=1
        MostrarListas(ConjLista, flag)
        #aux = Listadir[0]
        #Listadir[0] = Listaesq[0]
        #Listaesq[0] = aux
    return ConjLista, flag


        
def EmpilhaMeio(ConjLista,flag):
    '''
        Empilha meio está okay 
    '''
    flag+=1
    Listameio.append(Listaesq[0])
    Listaesq.remove(Listaesq[0])
    MostrarListas(ConjLista, flag)
    flag+=1
    Listameio.append(Listadir[0])
    Listadir.remove(Listadir[0])
    MostrarListas(ConjLista, flag)
    FimDeJogo(ConjLista, flag)
    ConjLista, flag = Desempilha(ConjLista, flag)
    MostrarListas(ConjLista, flag)
    flag+=1
    Listameio.append(Listadir[0])
    Listadir.remove(Listadir[0])
    MostrarListas(ConjLista, flag)
    flag+=1
    Listameio.append(Listaesq[0])
    Listaesq.remove(Listaesq[0])
    MostrarListas(ConjLista, flag)
    FimDeJogo(ConjLista, flag)
    ConjLista, flag = Desempilha(ConjLista, flag)
    MostrarListas(ConjLista, flag)
    return ConjLista, flag

def Empilhaesq(ConjLista, flag):
    ''' 
        Empilha a esquerda  okay 
    '''
    flag+=1
    Listaesq.append(Listadir[0])
    Listadir.remove(Listadir[0])
    MostrarListas(ConjLista, flag)
    flag+=1
    Listaesq.append(Listameio[0])
    Listameio.remove(Listameio[0])
    MostrarListas(ConjLista, flag)
    FimDeJogo(ConjLista, flag)
    ConjLista, flag = Desempilha(ConjLista, flag)
    MostrarListas(ConjLista, flag)
    flag+=1
    Listaesq.append(Listameio[0])
    Listameio.remove(Listameio[0])
    MostrarListas(ConjLista, flag)
    flag+=1
    Listaesq.append(Listadir[0])
    Listadir.remove(Listadir[0])
    MostrarListas(ConjLista, flag)
    FimDeJogo(ConjLista, flag)
    ConjLista, flag = Desempilha(ConjLista, flag)
    MostrarListas(ConjLista, flag)
    return ConjLista, flag

def Empilhadir(ConjLista, flag):
    ''' 
        Empilha a direita esta okay
    '''
    flag+=1
    Listadir.append(Listaesq[0])
    Listaesq.remove(Listaesq[0])
    MostrarListas(ConjLista, flag)
    flag+=1
    Listadir.append(Listameio[0])
    Listameio.remove(Listameio[0])
    MostrarListas(ConjLista, flag)
    FimDeJogo(ConjLista, flag)
    ConjLista, flag = Desempilha(ConjLista, flag)
    MostrarListas(ConjLista, flag)
    flag+=1
    Listadir.append(Listameio[0])
    Listameio.remove(Listameio[0])
    MostrarListas(ConjLista, flag)
    flag+=1
    Listadir.append(Listaesq[0])
    Listaesq.remove(Listaesq[0])
    MostrarListas(ConjLista, flag)
    FimDeJogo(ConjLista, flag)
    ConjLista, flag = Desempilha(ConjLista, flag)
    MostrarListas(ConjLista, flag)
    return ConjLista, flag

def InvertPossition(ConjLista, flag):
    aux = Listadir[0]
    Listadir[0] = Listameio[0]
    Listameio[0] = aux
    #MostrarListas(ConjLista, flag)
    return ConjLista,flag


ConjLista, flag = Desempilha(ConjLista,flag)
MostrarListas(ConjLista, flag)

#ConjLista, flag = Empilhaesq(ConjLista,flag)
ConjLista, flag = InvertPossition(ConjLista, flag) 
MostrarListas(ConjLista, flag)

NoEmpilhadoUm = 0
NoEmpilhadoDois = 0

# A B C ok
# A C B ok
# C A B ok
# C B A ok
# B A C ok
# B C A ok

while True:

    FimDeJogo(ConjLista, flag)
    ConjLista,flag = Desempilha(ConjLista,flag)
    ## empilha a esquerda 
    ## Ta fazendo okay 
    if(NoEmpilhadoUm != Listaesq[0]):
        ConjLista, flag = Empilhaesq(ConjLista, flag)
        empilhaesq = True
        NoEmpilhado = Listaesq[0]

    ## empilhando no meio primeiro 
    ## ta fazendo okay

    if(Listameio[0] != NoEmpilhado):
        ConjLista, flag = EmpilhaMeio(ConjLista, flag)
        empilhameio = True
        NoEmpilhadoDois = Listameio[0]

    ## empilha na direita
    if(Listadir[0] != NoEmpilhadoUm and Listadir[0]!=NoEmpilhadoDois): 
        ConjLista, flag = Empilhadir(ConjLista,flag)
        empilhadir = True

    ConjLista, flag = InvertPossition(ConjLista, flag)
