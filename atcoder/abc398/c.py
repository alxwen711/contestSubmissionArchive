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
d = {}
for i in range(n):
    if d.get(ar[i]) == None: d[ar[i]] = i
    else: d[ar[i]] = -1
ans = -1
for j in d.keys():
    if d[j] != -1: ans = max(ans,j)
if ans == -1: print(-1)
else: print(d[ans]+1)
