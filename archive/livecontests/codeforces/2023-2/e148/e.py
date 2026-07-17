import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#based on the k value maybe find k = 1, k = 2, k = 3... ???
mod = 998244353
n,a,x,y,m,k = readints()
ar = [a]
for i in range(n-1):
    ar.append((ar[-1]*x+y) % m)
s = 0
t = 0
br = list()
for j in range(n):
    t = (t+ar[j]) % mod
    s = (s+t) % mod
    br.append(s)
#print(ar)
#print(br)
for v in range(2,k+1):
    cr = [0]*n
    index = v-2
    s = 0
    t = 0
    for w in range(v-1,n):
        t = (t+br[index]) % mod
        #s = (s+t) % mod
        cr[w] = t
        index += 1
    br = cr
    #print(cr)
ans = 0
for uu in range(n):
    xy = br[uu]*(uu+1)
    ans = ans ^ xy
print(ans)
    
