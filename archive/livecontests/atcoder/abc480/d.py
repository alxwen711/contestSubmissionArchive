import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
a1 a1 a2 a1 a2 a3 a1 a2 a3 a4 ...

use some sort of prefixing system
"""

n,q = readints()
ar = readar()
prefix = [0]
for i in ar:
    prefix.append(prefix[-1]+i)

sumar = [0]
indexval = [0]
for j in range(1,n+1):
    sumar.append(sumar[j-1]+prefix[j])
    indexval.append(indexval[j-1]+j)

for _ in range(q):
    l,r = readints()
    # add f(r) subtract f(l-1)
    l -= 1
    low,high = 0,n
    ans = 0
    while high-low > 1:
        mid = (low+high)//2
        if indexval[mid] <= r: low = mid
        else: high = mid
    if indexval[high] <= r:
        ans = sumar[high]+prefix[r-indexval[high]]
    else:
        ans = sumar[low]+prefix[r-indexval[low]]
    low,high = 0,n
    while high-low > 1:
        mid = (low+high)//2
        if indexval[mid] <= l: low = mid
        else: high = mid
    if indexval[high] <= l:
        ans -= (sumar[high]+prefix[l-indexval[high]])
    else:
        ans -= (sumar[low]+prefix[l-indexval[low]])
    print(ans)
    


        
    
