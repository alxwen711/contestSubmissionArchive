import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,a,b = readints()
ar = readar()
l = a+b
br = list()
for i in range(n):
    x = ar[i] % l
    br.append(x)
br.sort()
ans = "No"
#print(br)
for j in range(n-1):
    mi,ma = br[j],br[j+1]
    r = l-ma+mi+1
    if r <= a:
        #print(mi,ma)
        ans = "Yes"
        break

mi,ma = br[0],br[-1]
r = ma-mi+1
if r <= a:
    ans = "Yes"

print(ans)
