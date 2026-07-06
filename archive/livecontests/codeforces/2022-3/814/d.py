import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1000
1110
0011
0101

5 0 3 2 4
create maximum number of subarrays out of array where xor is 0
"""

def bfunc(x, ar) -> bool:
    #for example use
    if x >= ar: return True
    return False


def bsearch(low, high, ar):
    while high - low > 1:
        mid = (low+high)//2 
        if bfunc(mid,ar): high = mid
        else: low = mid
    
    #diff is small enough
    if bfunc(low,ar): return low
    else: return high

for i in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    tmp = {}
    hit = False
    x = 0
    for j in range(n):
        y = ar[j] 
        if y == 0: hit = True
        x = x ^ y
        if x == 0: hit = True
        elif tmp.get(x) != None: hit = True
        else: tmp[x] = 42069
        if hit:
            hit = False
            ans += 1
            tmp = {}
            x = 0
    print(n-ans)
        
