import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n is at most 100, so having O(1) on a 2d setup is viable
"""

def d(n,ar):
    dp = list()
    tmp = list()
    prev = 0
    for i in range(n):
        tmp.append(ar[0][i]+prev)
        prev += ar[0][i]
    dp.append(tmp)
    for j in range(1,n):
        tmp = list()
        prev = 0
        for k in range(n):
            tmp.append(dp[-1][k]+ar[j][k]+prev)
            prev += ar[j][k]
        dp.append(tmp)
    return dp

n = readint()
ar = list()
br = list()
for _ in range(n):
    tmp = list()
    for _ in range(n):
        tmp2 = readar()
        tmp.append(tmp2)
    ar.append(tmp)
    br.append(d(n,tmp))

for _ in range(readint()):
    a,b,c,d,e,f = readints()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    e -= 1
    f -= 1
    ans = 0
    for x in range(a,b+1):
        ans += br[x][d][f]
        if c != 0:
            ans -= br[x][c-1][f]
        if e != 0:
            ans -= br[x][d][e-1]
        if c != 0 and e != 0:
            ans += br[x][c-1][e-1]
    print(ans)
