import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

m = readint()
ar = readar()
n = readint()
br = readar()

ar.sort() #use lowest discount
v = ar[0]
br.sort()
q,r = n//(v+2), n % (v+2)
ans = sum(br)
br.reverse()
for i in range(q):
    ans -= br[i*(v+2)+v]
    ans -= br[i*(v+2)+v+1]

if r == v+1: ans -= br[-1]
print(ans)
