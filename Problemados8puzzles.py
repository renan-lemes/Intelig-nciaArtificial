
''' 
    Trabalho de Inteligencia Artificial

    Nome : Renan Lemes Leepkaln
'''


Estado_fin = [['1', '2', '3'],
                ['4', '5', '6'], 
                ['7', '8', '_']]

Estado_ini = [['5', '8', '7'],
              ['4', '2', '3'], 
              ['6', '1', '_']]

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

def mov(Est, n):
    n += 1
    #
    ''' 3 down
    temp = Est[1][2]
    Est[1][2] = Est[2][2]
    Est[2][2] = temp 
    
    '''

    '''
    temp = Est[2][1]
    Est[2][1] = Est[2][2]
    Est[2][2] = temp 
    '''

    return Est, n   

#print(func_h(Estado_ini,Estado_fin))

Estado_ini, n = mov(Estado_ini, n)
SprintEstado(Estado_ini, n)