import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
each proper build has paired dominoes
"""

def solve(n,m,v,h):
    ans = list()
    for i in range(n):
        tmp = ["."]*m
        ans.append(tmp)
    for j in v.keys():
        x = len(v[j]) 
        if x % 2 == 1:
            print(-1)
            return
        for ii in range(x//2):
            ans[j][v[j][ii*2]] = "W"
            ans[j+1][v[j][ii*2]] = "B"
            ans[j][v[j][ii*2+1]] = "B"
            ans[j+1][v[j][ii*2+1]] = "W"
    for k in h.keys():
        x = len(h[k]) 
        if x % 2 == 1:
            print(-1)
            return
        for jj in range(x//2):
            ans[h[k][jj*2]][k] = "W"
            ans[h[k][jj*2]][k+1] = "B"
            ans[h[k][jj*2+1]][k] = "B"
            ans[h[k][jj*2+1]][k+1] = "W"
    for y in range(n):
        print(*ans[y],sep="")
    return
            
            
for i in range(readint()):
    n,m = readints()
    v = {}
    h = {}
    for j in range(n):
        s = sys.stdin.readline()
        for k in range(m):
            if s[k] == "U": #vertical
                if v.get(j) == None: v[j] = list()
                v[j].append(k)
            elif s[k] == "L": #horizontal
                if h.get(k) == None: h[k] = list()
                h[k].append(j)
    solve(n,m,v,h)
    
