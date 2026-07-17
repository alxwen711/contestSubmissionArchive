import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
small case size makes this brute forcable
"""

class Node:
    def __init__(self):
        self.parent = None
        self.state = 0
        self.used = 0 # bin check
        self.score = 0
        self.best = 0

ar = list()
for _ in range(3):
    tmp = readar()
    ar.append(tmp)

def checkwin(ar):
    if ar[0][0] == ar[1][1] == ar[2][2] and ar[0][0] != -1:
        if ar[0][0] == 0: return 1000000000000
        else: return -1000000000000
    elif ar[0][0] == ar[0][1] == ar[0][2] and ar[0][0] != -1:
        if ar[0][0] == 0: return 1000000000000
        else: return -1000000000000
    elif ar[1][0] == ar[1][1] == ar[1][2] and ar[1][0] != -1:
        if ar[1][0] == 0: return 1000000000000
        else: return -1000000000000
    elif ar[2][0] == ar[1][1] == ar[0][2] and ar[2][0] != -1:
        if ar[2][0] == 0: return 1000000000000
        else: return -1000000000000
    elif ar[2][0] == ar[2][1] == ar[2][2] and ar[2][0] != -1:
        if ar[2][0] == 0: return 1000000000000
        else: return -1000000000000
    elif ar[0][0] == ar[1][0] == ar[2][0] and ar[0][0] != -1:
        if ar[0][0] == 0: return 1000000000000
        else: return -1000000000000
    elif ar[0][1] == ar[1][1] == ar[2][1] and ar[0][1] != -1:
        if ar[0][1] == 0: return 1000000000000
        else: return -1000000000000
    elif ar[0][2] == ar[1][2] == ar[2][2] and ar[0][2] != -1:
        if ar[0][2] == 0: return 1000000000000
        else: return -1000000000000
    return 0
    

def rate(ns,ar):
    check = checkwin(ns)
    if check != 0: return check
    x = 0
    for i in range(3):
        for j in range(3):
            if ns[i][j] == 0: x += ar[i][j]
            elif ns[i][j] == 1: x -= ar[i][j]
    return x

def genboard(x):
    cr = list()
    for i in range(3):
        tmp = list()
        for j in range(3):
            xv = x % 3
            xv -= 1
            tmp.append(xv)
            x //= 3
        cr.append(tmp)
    return cr

scores = list()
# compute all board states
for snth in range(3**9):
    scores.append(rate(genboard(snth),ar))
states = list()
states.append([Node()])
m = 0
for i in range(9):

    level = list()
    for prev in states[-1]:
        if abs(prev.score) != 1000000000000: #not auto win
            b = 1
            for a in range(9):
                if prev.used & b == 0:
                    nn = Node()
                    nn.used = prev.used + b
                    nn.state = prev.state + ((3**a)*(m+1)) # cause of death: this was prev.used before. ffs.
                    nn.score = scores[nn.state]
                    nn.best = nn.score
                    nn.parent = prev
                    level.append(nn)
                b *= 2
    states.append(level)
    m ^= 1

    """
    if s.parent != p: # first child
            p = s.parent
            s.parent.best = s.best
        else:
    
    """
p = None
for j in range(9,0,-1):
    for s in states[j]:
        if s.parent != p: # first child
            p = s.parent
            s.parent.best = s.best
        else:
            if j % 2 == 1: s.parent.best = max(s.parent.best,s.best)
            else: s.parent.best = min(s.parent.best,s.best)
ans = states[0][0].best
#print(ans)
#index = 0
#for i in states[1]:
#    print(i.best,i.used,i.state,scores[i.state])
#    index += 1

if ans > 0: print("Takahashi")
else: print("Aoki")
