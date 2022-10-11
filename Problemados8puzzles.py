
''' 
    Trabalho de Inteligencia Artificial

    Nome : Renan Lemes Leepkaln
'''


Estado_fin = [['1', '2', '3'],
              ['4', '_', '5'], 
              ['6', '7', '8']]

Estado_ini = [['1', '2', '3'],
              ['7', '_', '5'], 
              ['8', '6', '4']]

n = 0


def SprintEstado(Est, n):
    print('----------------------------------')
    print('  movimento:', n)
    for i in range(len(Est)):
        print(Est[i])
        if i > 2 or i > 4:
            print('\n')
    print('----------------------------------')


SprintEstado(Estado_ini, n)

def func_h(Est_i, Est_f):
    h = 0
    for i in range(len(Est_i)):
        for j in range(len(Est_i[i])):
            if Est_f[i][j] != Est_i[i][j]:
                h += 1

    return h 

def Busca_(Est_i):
    for i in range(len(Est_i)):
        for j in range(len(Est_i[i])):
            if Est_i[i][j] == "_":
                return i, j 

def Verifica_estado(Est_i, Est_f):
    for i in range(len(Est_f)):
        for j in range(len(Est_f[i])):
            if Est_f[i][j] != Est_i[i][j]:
                return i,j

def mov_9(Est, n):
    ''' 
        Est: estado da matriz
        n: quantidade de movimentos
    
    '''

    # moviemnto 1
    temp = Est[1][2]
    Est[1][2] = Est[2][2]
    Est[2][2] = temp 
    
    # movimento 2
    temp = Est[2][1]
    Est[2][1] = Est[2][2]
    Est[2][2] = temp 

    return Est, n    

def mov_8(Est, n):
    
    # movimento 1
    temp = Est[2][2]
    Est[2][2] = Est[2][1]
    Est[2][1] = temp
    
    # movimento 2
    temp = Est[2][0]
    Est[2][0] = Est[2][1]
    Est[2][1] = temp 

    # movimento 3
    temp = Est[1][1]
    Est[1][1] = Est[2][1]
    Est[2][1] = temp

    return Est, n

def mov_7(Est, n):
     # movimento 1
    temp = Est[1][0]
    Est[1][0] = Est[2][0]
    Est[2][0] = temp 
    
    # movimento 2
    temp = Est[2][1]
    Est[2][1] = Est[2][0]
    Est[2][0] = temp

    return Est, n

def mov_6(Est, n):
    
    # movimento 1
    temp = Est[0][2]
    Est[0][2] = Est[1][2]
    Est[1][2] = temp
    
    # movimento 2
    temp = Est[1][1]
    Est[1][1] = Est[1][2]
    Est[1][2] = temp

    # movimento 3
    temp = Est[2][2]
    Est[2][2] = Est[1][2]
    Est[1][2] = temp

    return Est, n

def mov_5(Est, n):
    
    # movimento 1
    temp = Est[1][2]
    Est[1][2] = Est[1][1]
    Est[1][1] = temp 
    
    
    # movimento 2 
    temp = Est[2][1]
    Est[2][1] = Est[1][1]
    Est[1][1] = temp
    
    
    # movimento 3 
    temp = Est[1][0]
    Est[1][0] = Est[1][1]
    Est[1][1] = temp
    

    # movimento 4 
    temp = Est[0][1]
    Est[0][1] = Est[1][1]
    Est[1][1] = temp
   
    return Est, n


def mov_4(Est, n):
    

    # movimento 1
    temp = Est[2][0]
    Est[2][0] = Est[1][0]
    Est[1][0] = temp
    
    # movimento 2
    temp  = Est[1][1]
    Est[1][1] = Est[1][0]
    Est[1][0] = temp
    
    # movimento 3
    temp = Est[0][0]
    Est[0][0] = Est[1][0]
    Est[1][0] = temp
    
    return Est, n


def mov_3(Est, n):
    
    # movimento 1
    temp = Est[1][2]
    Est[1][2] = Est[0][2]
    Est[0][2] = temp

    # movimento 2
    temp = Est[0][1]
    Est[0][1] = Est[0][2]
    Est[0][2] = temp

    return Est, n


def mov_2(Est, n):
    
    # movimento 1
    temp = Est[0][2]
    Est[0][2] = Est[0][1]
    Est[0][1] = temp

    
    # movimento 2
    temp = Est[1][1]
    Est[1][1] = Est[0][1]
    Est[0][1] = temp


    # movimento 3
    temp = Est[0][0]
    Est[0][0] = Est[0][1]
    Est[0][1] = temp

    return Est, n

def mov_1(Est, n):
    
    #movimento 1
    temp = Est[0][1]
    Est[0][1] = Est[0][0]
    Est[0][0] = temp

    # movimento 2
    temp = Est[1][0]
    Est[1][0] = Est[0][0]
    Est[0][0] = temp

    return Est, n




def mov(Est,Est_f ,  n):
    n += 1

    _ = (Busca_(Est))
    v = Verifica_estado(Est, Est_f)
    
    ''' 
    if _ == (0, 0):
        Est, n = mov_1(Est, n)
    if _ == (0,1):
        Est, n = mov_2(Est, n)
    if _ == (0,2):
        Est, n = mov_3(Est, n)
    if _ == (1,0):
        Est, n = mov_4(Est, n)
    if _ == (1,1):
        Est, n = mov_5(Est, n)
    if _ == (1,2):
        Est, n = mov_6(Est, n)
    if _ == (2,0):
        Est, n = mov_7(Est, n)
    if _ == (2, 1):
        Est, n = mov_8(Est, n)
    if _ == (2, 2):
        Est, n = mov_9(Est, n)  
    '''
    
    
    return Est, n 
      

#print(func_h(Estado_ini,Estado_fin))

Estado_ini, n = mov(Estado_ini, Estado_fin, n)
SprintEstado(Estado_ini, n)

