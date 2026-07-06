import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from itertools import permutations

"""
2
4 = 2 + 2
12 = 1*4 + 2*2 + 4*1
32 = 1*12 + 2*4 + 4*2 + 12*1
100
312
1076
3772

2,8,20,68,212,764,2696

[almost perfect,n] = almost perfect
[ap,n,n-1] = ap

0,0,2,6,24,80,312,1152
0,0,2,2, 8,20,104, 368 
(previous 2 values)*2
"""
def check(ar,b):
    br = [0]*b
    for s in range(b):
        br[ar[s]] = s
    for t in range(b):
        if abs(ar[t]-br[t]) > 1: return 0
    """if b < 8:
        for ll in range(b):
            if abs(ar[ll]-br[ll]) == 1:
                print(ar)
                break"""
    return 1
aar = list()
for i in range(2,10):
    ar = list()
    for j in range(i):
        ar.append(j)
    br = list(permutations(ar))
    ans = 0
    for k in range(len(br)):
        ans += check(br[k],i)
    print(i,ans)
    aar.append(ans)

r = list()
r.append(2)
r.append(4)
for i in range(6):
    r.append(r[-1]+r[-2]*(len(r)+1)+2)
print(aar)
print(r)
