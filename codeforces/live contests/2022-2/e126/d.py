import sys
from math import ceil
n,k = map(int,sys.stdin.readline().split())
ar = list(map(int,sys.stdin.readline().split()))
x = len(ar)
ans = 0
for i in range(x-k+1):
    if ar[i] > 0:
        dec = ar[i]
        ans += dec
        for j in range(k):
            ar[i+j] -= (dec*(j+1))
inc = 0
for l in range(k):
    tmp = int(ceil(ar[x-k+l]/(l+1)))
    if tmp > inc: inc = tmp
ans += inc
print(ans)
