''' 
    Aluno: Renan Lemes Leepkaln
    font-article: https://cadernodelaboratorio.com.br/o-que-sao-os-algoritmos-geneticos/
    

    Explicando o algoritmo:
    o algoritmo é apenas um jogo da forca com o a IA
    no caso ela tem que adivinhar qual é a frase que colocarmos pra ela.
'''
from random import randint
from random import random

def newChar():
    r = randint(63,122)
    if r == 64:
        r = ord(' ')
    if r == 63:
        r = ord('.')
        
    return chr(r)
def mapit(i,m,M, a = 0, b = 1):
    return (b - a)*(i - m)/(M-m)

  
  
class DNA:
    def __init__(self, num):
        self.num = num
        self.genes = [newChar() for i in range(num)]
        self.fitnes = 0
    
    def getPhrase(self):
        s = ''
        return s.join(self.genes)
    
    def calcFitness(self, target):
        scor = 0
        for idx, gen in enumerate(self.genes):
            if gen == target[idx]:
                scor += 1
        self.score = scor/len(target)
        return scor/len(target)
    
    def Reproduction(self, partner):
        child = DNA(self.num)
        midpoint = randint(0, len(self.genes))
        for i in range(self.num):
            if i < midpoint: 
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child
    
    def mutate(self, mutRate):
        for i in range(self.num):
            r = random()
            if r < mutRate:
                self.genes[i] = newChar()



class Papulation:
    def __init__(self, target, pmax, mutationRate, max_mat_pool = 1e5):
        self.target = target
        self.pmax = pmax
        self.mutationRate = mutationRate
        self.papulation = []
        for i in range(pmax):
            self.papulation.append(DNA(len(target)))
        self.matinPool = []
        self.bestfit = None
        self.max_mat_pool = max_mat_pool
        
    def calcFitness(self):
        for i in self.papulation:
            i.calcFitness(self.target)
    def naturalSelaction(self):
        maxfit = 0
        for i in self.papulation:
            if i.score > maxfit:
                maxfit = i.score
                self.bestfit = i
                
        for i in self.papulation:
            n  = int(mapit(i.score, 0, maxfit)*100)
            for j in range(n):
                self.matinPool.append(i)
                
    def died(self):
        diff = int(len(self.matinPool) - self.max_mat_pool)
        if diff > 0:
            del self.matinPool[0:diff]
                
                
    def newGenration(self):
        for i in range(self.pmax):
            partnarA = self.matinPool[randint(0,len(self.matinPool) -1)]
            partnarB = self.matinPool[randint(0,len(self.matinPool) - 1)]
            child = partnarA.Reproduction(partnarB)
            child.mutate(self.mutationRate)
            self.papulation[i] = child

target = '''Inteligencia Artificial'''

pmax = 1000
mutationRate = 0.01
genrations = 1000

k = 0
p = Papulation(target,pmax, mutationRate)

for i in range(genrations):
    p.calcFitness()
    p.naturalSelaction()
    p.newGenration()
    if p.bestfit.getPhrase() == target:
        k+=1
#         print('**gen: ', i, p.bestfit.getPhrase())
    print('gin: ', i,  p.bestfit.getPhrase())
    p.died()