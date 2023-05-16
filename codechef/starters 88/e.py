import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

x = list()
y = list() # not actually needed
for i in range(readint()):
    xx,yy = readints()
    x.append(xx)
    y.append(yy)
nn = len(x)

d = {}
for j in range(nn):
    n = x[j]
    if d.get(n) == None: d[n] = 0
    d[n] += 1
    
ar = list(d.keys())
ar.sort()
br = list()
for k in ar:
    br.append(d[k])

index = 0
num,dom = 1,1
mod = 1000000007
c = nn
for m in range(nn):
    if br[index] == 0: index += 1
    dom = (dom*c) % mod
    num = (br[index]*num) % mod
    br[index] -= 1
    c -= 1
    #print(num,dom)
inv = pow(dom,mod-2,mod)
print(((inv*num) % mod))
