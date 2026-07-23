import sys
from math import gcd

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Either add or sub previous value any number of times
gcd is involved? first value has some importance
1 at the start -> 0 total
first value can never be changed, then remaining vals
would only be able to convert to some sort of modulo
gcd of first value and difference to second
many of these problems will then burn down to gcd 1 type scenarios
so that only the first two value's difference seems to matter?

gcd between values returns a closer approximate
if its lower or equal, can be cut off and spam rest of the way
otherwise we keep going (in the case that it must be a multiple of the previous)

this would be O(n^2), then determine how to optimize the multiple rule

possible to group identical values together, then worst case is repeating
chains of values which is probably O(n log n log n)
ie. basically it should be faster than O(n^1.5) I think?

2 4 2 4 2 4 2 4 2 4 2 4 breaks this (each 2 starting point can full chain)

binary search the longest gcd segment that works
"""

def create_seg(ar):
    seg = list()
    seg.append(ar)
    while len(seg[-1]) != 1:
        tmp = list()
        for i in range(len(seg[-1])//2):
            tmp.append(gcd(seg[-1][2*i],seg[-1][2*i+1]))
        seg.append(tmp)
    return seg

def query(seg,li,ri):
    ans = 0
    l,r = li,ri
    for i in range(len(seg)):
        if l > r: return ans
        if l % 2 == 1:
            ans = gcd(ans,seg[i][l])
            l += 1
        if r % 2 == 0:
            ans = gcd(ans,seg[i][r])
            r -= 1
        l //= 2
        r //= 2
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    seg = create_seg(ar)
    ans = 0
    for i in range(n-1):
        if query(seg,i,n-1) != ar[i]:
            # find minimal length such that gcd is NOT ar[i]
            low = i+1
            high = n-1
            while high-low > 1:
                mid = (low+high)//2
                if query(seg,i,mid) != ar[i]: high = mid
                else: low = mid
            index = low
            if query(seg,i,low) == ar[i]: index = high
            mv = ar[index] % ar[i]
            mv = min(mv,ar[i]-mv)
            ans += mv*(n-index)
    print(ans)







                    



    
