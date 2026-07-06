import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
br is maximums except for one
"""

def bruh(ar):
    a,b = -23456789564,-75678976547568
    for i in ar:
        if i > a:
            b = a
            a = i
        elif i > b:
            b = i
    return a,b
        

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    if n == 1:
        print(ar[0]+br[0])
        continue
    cr = list()
    dr = list()
    for i in range(n):
        if ar[i] > br[i]:
            cr.append(br[i])
            dr.append(ar[i])
        else:
            cr.append(ar[i])
            dr.append(br[i])
    ds = sum(dr)
    high,secondhigh = bruh(cr)
    ans = -9837493498329439
    for j in range(n):
        v = ds-dr[j]+cr[j]
        if cr[j] != high: v += max(dr[j],high)
        else: v += max(dr[j],secondhigh)        
        ans = max(ans,v)
    print(ans)
