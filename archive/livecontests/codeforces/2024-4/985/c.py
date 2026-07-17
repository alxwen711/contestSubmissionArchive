import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
lt binary on if a rating is reachable is possible?
not necessarily increasing rating every contest

1 2 3 2 3 4 3 4 3
1 2 3 3 3 4 4 4 4

once 2nd array is attained, use backwards shifting + hashing to O(1)
compute how the maximum ends up when going outwards after
assumes entering 2nd part with maximal value is optimal via greedy

Plan C: TRIPLE DP
"""


for _ in range(readint()):
    n = readint()
    ar = readar()
    br = [0]*n # before skip
    cr = [0]*n # during skip
    dr = [0]*n # after skip
    br[0] = 1
    dr[0] = -1
    for i in range(1,n):
        x = ar[i]
        # br
        b = br[i-1]
        if x > b: b += 1
        elif x < b: b -= 1
        br[i] = b
        # cr
        cr[i] = max(cr[i-1],br[i-1])
        # dr
        d = max(dr[i-1],cr[i-1])
        if x > d: d += 1
        elif x < d: d -= 1
        dr[i] = d
    print(max(dr[-1],0))
    
    
