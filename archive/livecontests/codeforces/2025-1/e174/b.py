import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def f(ar,br):
    n = len(ar)
    if n == 0: return 0
    if n == 1: return 1
    ar.sort()
    br.sort()
    for i in range(n-1):
        if ar[i][0] == ar[i+1][0] and ar[i][1]+1 == ar[i+1][1]: return 2
        if br[i][0] == br[i+1][0] and br[i][1]+1 == br[i+1][1]: return 2
    return 1

for _ in range(readint()):
    n,m = readints()
    grid = list()
    for _ in range(n):
        grid.append(readar())
    r,c = list(),list()
    for _ in range(n*m+1):
        tmp = list()
        r.append(tmp)
        tmp = list()
        c.append(tmp)
    for i in range(n):
        for j in range(m):
            r[grid[i][j]].append((i,j))
            c[grid[i][j]].append((j,i))
            
    ans = list()
    for k in range(n*m+1):
        ans.append(f(r[k],c[k]))
    ans.sort()
    ans.pop()
    print(sum(ans))
