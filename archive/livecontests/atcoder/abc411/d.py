import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1 = server to pc
2 = append to pc
3 = pc to server

op 3: move pc ending to perma, set server pt to pc
op 1: remove pc ending, set base to server
op 2: add to ending

to retrieve, go to each pt until -1 is hit
"""

class pc:
    def __init__(self):
        self.ending = ""
        self.perma = ""
        self.base = -1

n,q = readints()
pcs = list()
serverpt = -1
for _ in range(n):
    pcs.append(pc())
for _ in range(q):
    ar = list(readins())
    x = int(ar[0])
    y = int(ar[1])-1
    if x == 1 and y != serverpt:
        pcs[y].base = serverpt
        pcs[y].ending = ""
        pcs[y].perma = ""
    elif x == 2:
        pcs[y].ending = "".join([pcs[y].ending,ar[2]])
    else:
        pcs[y].perma = "".join([pcs[y].perma,pcs[y].ending])
        pcs[y].ending = ""
        serverpt = y
ans = list()
for _ in range(200003):
    if serverpt == -1: break
    ans.append(pcs[serverpt].perma)
    serverpt = pcs[serverpt].base
ans.reverse()
print(*ans,sep="")
    
