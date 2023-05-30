import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
d = {}
for i in range(n):
    x = ar[i]
    if d.get(x) == None: d[x] = list()
    d[x].append(i)
br = list()
for j in d.keys():
    if len(d[j]) != 1: br.append((d[j][0],d[j][-1]))
br.sort()
m = n-1
if len(br) != 0:
    st = br[0][0]
    ed = br[0][1]
    for k in range(1,len(br)):
        if br[k][0] < ed:
            ed = max(ed,br[k][1])
        else:
            m -= (ed-st)
            st = br[k][0]
            ed = br[k][1]
    m -= (ed-st)
print(pow(2,m,998244353))
            
