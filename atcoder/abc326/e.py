import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
cr = readar()
ar = [0]*(n+1)
for i in range(n):
    ar[i+1] = cr[i]
br = [0]*(n+1)
m = 998244353
inv = pow(n,m-2,m)

t = 0
for j in range(n-1,-1,-1):
    t = (t+ar[j+1]) % m
    br[j] = (t*inv) % m
    t = (t+br[j]) % m
print(br[0])
