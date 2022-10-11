
from re import A
import timeit
import random
import copy

from regex import P

''' 
    [[1,0,4]
     [5,2,8]
     [7,6,3]   
    ]
'''

goal = []
goal.append([1,2,3])
goal.append([4,5,6])
goal.append([7,8,0])




class No:
    def __init__(self, state, no_f, g, h):
        self.state = state
        self.f = no_f
        self.g = g
        self.h = h
    
    def __eq__(self, o):
        ''' 
            Verifica se o no é igual ao outro 
        '''
        return self.state == o.state

    def __repr__(self):
        ''' 
            Mostra o no
        '''
       
        return str(self.state)

    def getState(self):
        ''' 
            Retorna o Estado do no
        '''
        return self.state

def Soluction(list_):
    invert = 0
    for i,e in enumerate(list_):
        if e == 0:
            continue
        for j in range(i+1, len(list_)):
            if list_[j] == 0:
                continue
            if e > list_[j]:
                invert += 1
    if invert%2 == 1:
        return False
    else: 
        return True


def geraInit(st=goal[:]):
    list_ = [j for i in st for j in i]
    while True:
            
        random.shuffle(list_)
        st = [list_[:3]]+[list_[3:6]]+[list_[6:]]
        if Soluction(list_) and st!= goal:return st
    return 0

#print(geraInit(goal))

def Localization(state, element = 0):
    for i in range(3):
        for j in range(3):
            if state[i][j] == element:
                lin = i
                col = j
                return lin, col

def Dist(st1, st2):
    ''' 
        Distancia Taxista.
        d = | a - b | 
    '''
    dist = 0
    step = 0
    for i in range(3):
        for j in range(3):
            if st1[i][j] == 0: continue
            i2, j2 = Localization(st2, st1[i][j])
            if i2 != i or j2 != j: step =+ 1
            dist += abs(i2 - i) + abs(j2 -j)
    return dist + step


def Creat_no(state, no_f, g=0):
    h = g + Dist(state, goal)
    return No(state, no_f, g, h)

def Inset_No(no, front):
    ''' 
        Organiza a fronteira dos nós com base na menor distância taxista.
    '''
    if no in front:
        return front
    front.append(no)
    keys = front[-1]
    j = len(front) -2
    while front[j].h > keys.h and j>=0:
        front[j+1] = front[j]
        front[j] = keys
        j -=1
    return front

def Mov_Donw(state):
    lin, col = Localization(state)
    if lin < 2:
        state[lin+1][col], state[lin][col] = state[lin][col] , state[lin+1][col]
    return state

def Mov_Up(state):
    lin, col = Localization(state)
    if lin > 0:
        state[lin-1][col], state[lin][col] = state[lin][col], state[lin-1][col]
    return state

def Mov_Right(state):
    lin, col = Localization(state)
    if col < 2:
        state[lin][col+1], state[lin][col] = state[lin][col], state[lin][col+1]
    return state

def Mov_left(state):
    lin, col = Localization(state)
    if col > 0:
        state[lin][col-1], state[lin][col] = state[lin][col], state[lin][col-1]
    return state

def Return_No(no):
    ''' 
        Função sucessor calcula todos os estados a partir dos sucessores do no
        coloca em uma lista e retorna ela 
    '''
    state = no.state
    fat = no.f
    if fat:
        stateF = fat.state
    else:
        stateF = None
    list_S = []
    l1 = Mov_Up(copy.deepcopy(state))
    if l1 != state:
        list_S.append(l1)
    l2 = Mov_Right(copy.deepcopy(state))
    if l2 != state:
        list_S.append(l2)
    l3 = Mov_Donw(copy.deepcopy(state))
    if l3 != state:
        list_S.append(l3)
    l4 = Mov_left(copy.deepcopy(state))
    if l4 != state:
        list_S.append(l4)
    return list_S

def Search(max, no_init):
   #print(no_init, ":")
    nmov = 0
    bord = [no_init]
    while bord:
        no = bord.pop(0)
        if no.state == goal:
            sol = []
            while True:
                sol.append(no.state)
                no = no.f
                if not no: break
            sol.reverse()
            return sol, nmov
        nmov +=1
        if (nmov%(max/10)) == 0: print(nmov, end="....")
        if nmov>max: break
        sucs = Return_No(no)
        for s in sucs:
            Inset_No(Creat_no(s, no, no.g+1), bord)
    
    return 0, nmov                

def InitiPuzzle(maxD, n_amost):
    tim = []
    solutions = []
    solut = []
    not_solutions = []
    nS = 0
    nNs = 0

    for i in range(n_amost):
        noInit = Creat_no(geraInit(), None)
        state_time = timeit.default_timer()
        res, nmov = Search(maxD, noInit)
        timer = timeit.default_timer() - state_time
        if res:
            solut.append(res)
            print("\nSolucionado em {} segundos e {} movimentos".format(timer, nmov))
            tim.append(timer)
            solutions.append((noInit.state, nmov))
            nS +=1
        else:
            print("\nFalhou em {} segundos e {} movimentos".format(timer, nmov))
            not_solutions.append((noInit.state, nmov))
            tim.append(None)
            nNs +=1
    print("Solucionados {} e não solucionados {} ".format(nS,nNs))
    return tim, solutions, solut, not_solutions, nS, nNs


sol = InitiPuzzle(3000, 1)
a = repr(sol)

print(len(a))
print(a)
