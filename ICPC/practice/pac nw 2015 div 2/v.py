import sys
from math import gcd

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
odd chain: negative ratio
even chain: positive ratio
paint the gears with 1/0
any triangle still breaks the system
"""

class gear:
    def __init__(self,x,y,r):
        self.r = r
        self.x = x
        self.y = y
        self.neighbours = list() #index list
        self.colour = -1

def adj(a,b):
    return abs(a.x-b.x)**2+abs(a.y-b.y)**2 == (a.r+b.r)**2

def verify(g):
    for i in range(len(g)):
        if g[i].colour != -1:
            for j in range(len(g[i].neighbours)):
                if g[i].colour == g[g[i].neighbours[j]].colour: return False
    return True


n = readint()
gears = list()
for i in range(n):
    a,b,c = readints()
    gears.append(gear(a,b,c))

for aa in range(n-1):
    for bb in range(aa+1,n):
        if adj(gears[aa],gears[bb]):
            gears[aa].neighbours.append(bb)
            gears[bb].neighbours.append(aa)

q = [0]
gears[0].colour = 0
while len(q) != 0:
    g = q.pop()
    for j in range(len(gears[g].neighbours)):
        xx = gears[g].neighbours[j]
        if gears[xx].colour == -1:
            q.append(xx)
            gears[xx].colour = gears[g].colour ^ 1
    
    
if not verify(gears): print("The input gear cannot move.")
elif gears[-1].colour == -1: print("The input gear is not connected to the output gear.")
else:
    #can move, figure out ratio and other shenanigans
    a,b = gears[0].r,gears[-1].r
    cccc = gcd(a,b)
    a //= cccc
    b //= cccc
    if gears[-1].colour == 0: print(str(a)+":"+str(b))
    else: print("-"+str(a)+":"+str(b))
            
