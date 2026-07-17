import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
for each medicine, compute what cells are reachable
then beginning from start, determine what medicines can be hit,
for each one include in area that can be reached,
repeat until goal found or no more possible medicine
"""

class queue:
    def __init__(self,limit=100000):
        self.q = list()
        self.pt = 0
        self.l = 0
        self.memRefresh = limit

    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        #check if memory needs to be refreshed
        if self.pt == self.memRefresh:
            self.pt = 0
            self.l -= self.memRefresh
            self.q = self.q[self.memRefresh:]
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self) -> int:
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l



def ff(ar,a,b,c):
    ar[a][b] = 0
    q = queue()
    q.add((a,b))
    ans = list()
    ans.append((a,b))
    while not q.empty():
        x = q.dequeue()
        i,j = x[0],x[1]
        v = ar[i][j]
        if v < c: # can go further
            if i != 0:
                if ar[i-1][j] == -1:
                    ar[i-1][j] = v+1
                    ans.append((i-1,j))
                    q.add((i-1,j))
            if i != len(ar)-1:
                if ar[i+1][j] == -1:
                    ar[i+1][j] = v+1
                    ans.append((i+1,j))
                    q.add((i+1,j))
            if j != 0:
                if ar[i][j-1] == -1:
                    ar[i][j-1] = v+1
                    ans.append((i,j-1))
                    q.add((i,j-1))
            if j != len(ar[0])-1:
                if ar[i][j+1] == -1:
                    ar[i][j+1] = v+1
                    ans.append((i,j+1))
                    q.add((i,j+1))
    return ans
            
    

def solve(h,w,grid):
    # reformat grid
    sx,sy = 0,0
    ex,ey = 0,0
    ar = list()
    for i in range(h):
        tmp = list()
        for j in range(w):
            cc = grid[i][j]
            if cc == "S":
                sx,sy = i,j
            if cc == "T":
                ex,ey = i,j
            if cc == "#": tmp.append(-2)
            else: tmp.append(-1)
        ar.append(tmp)
    n = readint()
    used = {}
    d = {} # all positions covered
    for _ in range(n):
        r,c,e = readints()
        r -= 1
        c -= 1
        used[(r,c)] = False
        d[(r,c)] = ff(deepcopy(ar),r,c,e)
    if used.get((sx,sy)) == None: return "No"
    used[(sx,sy)] = True
    q = [(sx,sy)]
    while len(q) != 0:
        x = q.pop()
        a,b = x[0],x[1]
        for p in d[(a,b)]:
            xx,yy = p[0],p[1]
            if ar[xx][yy] == -1:
                ar[xx][yy] = 1
                if xx == ex and yy == ey: return "Yes"
                if used.get((xx,yy)) == False:
                    used[(xx,yy)] = True
                    q.append((xx,yy))
    return "No"

    
h,w = readints()
grid = list()
for _ in range(h):
    s = input()
    grid.append(s)
print(solve(h,w,grid))
