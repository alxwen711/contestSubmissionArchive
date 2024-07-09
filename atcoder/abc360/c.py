import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = readar()
br = readar()
d = {}
ans = 0
for i in range(n):
    x,y = ar[i],br[i]
    if d.get(x) == None: d[x] = y
    elif d[x] > y: ans += y
    else:
        ans += d[x]
        d[x] = y
print(ans)
