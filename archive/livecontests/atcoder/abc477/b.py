import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,d = readints()
br = readar()
ar = list()
for ii in range(n):
    ar.append((br[ii],ii+1))
ar.sort()
ans = list()
if ar[1][0]-ar[0][0] >= d: ans.append(ar[0][1])
if ar[-1][0]-ar[-2][0] >= d: ans.append(ar[-1][1])
for i in range(1,n-1):
    if ar[i][0]-ar[i-1][0] >= d and ar[i+1][0]-ar[i][0] >= d: ans.append(ar[i][1])
print(len(ans))
ans.sort()
print(*ans)

