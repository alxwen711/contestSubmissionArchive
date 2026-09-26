import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
y K-dollar bills, x 1-dollar bills

K-dollar bills can only be used on drinks (br)

two pointers, try buying 0/1/2... lowest drinks
then move ar pointer for number of desserts
if drink cost is impossible, tried all setups, stop
"""

n,m,k = readints()
x,y = readints()
ar = readar()
br = readar()

ar.sort()
br.sort()

tc = 0
ap = 0

while ap != n:
    if (tc+ar[ap]) <= (x+(y*k)):
        tc += ar[ap]
        ap += 1
    else: break

ans = ap
for i in range(m):
    r = (br[i]+k-1)//k
    if r > y: break
    paid = r*k
    y -= r
    x += (paid-br[i])
    while ap != 0:
        if tc > (x+(y*k)):
            ap -= 1
            tc -= ar[ap]
        else: break
    ans = max(ans,ap+i+1)
print(ans)




    
