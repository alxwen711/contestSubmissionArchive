import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
answer is always at most 31
it is always most optimal to get the lower bits to 1 first
O(n log n log n) is fast enough
"""

def mi(n,ar):
    index = -1
    highest = -2
    for i in range(n):
        if ar[i] > highest:
            index = i
            highest = ar[i]
    return highest,index

def f(n,ar,l,bit):
    ans = 0
    bitmask = 2**(l+1)-1 # l+1 1's
    br = list()
    for a in ar:
        br.append(a & bitmask)
    while len(bit) != (l+1):
        bit.pop()
    for k in range(l,-1,-1):
        val = 2**k
        if bit[k] == 0: # get this bit in somehow
            x,index = mi(n,br)
            for ii in range(k+1):
                bit[ii] -= (x % 2)
                x //= 2
            bit[k] += 1
            ans += (val-br[index])
            br[index] = val
        # eliminate anything with this bit
        for m in range(n):
            if br[m] & val != 0:
                br[m] -= val
                bit[k] -= 1
        bit.pop()
    return ans

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    bit = [0]*31 # 2**31 > 2 billion, never possible
    for i in ar:
        x = i
        for j in range(31):
            bit[j] += (x % 2)
            x //= 2
    ans = [9999999999999999]*32
    s = 0
    for snth in range(31):
        if bit[snth] != 0:
            s += 1
    for k in range(s+1):
        ans[k] = 0
    for l in range(31):
        if bit[l] == 0:
            s += 1
            ans[s] = f(n,ar,l,deepcopy(bit))
    #print(ans)
    # answer queries
    for _ in range(q):
        x = readint()
        low = 0
        high = 31
        while high-low > 1:
            mid = (low+high)//2
            if ans[mid] <= x: low = mid
            else: high = mid
        if ans[high] <= x: print(high)
        else: print(low)
