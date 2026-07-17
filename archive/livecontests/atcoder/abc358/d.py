import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = readar()
br = readar()
ar.sort()
br.sort()
bindex = 0
ans = 0
for i in range(n):
    if bindex == m: break
    if ar[i] >= br[bindex]:
        ans += ar[i]
        bindex += 1
if bindex == m: print(ans)
else: print(-1)
