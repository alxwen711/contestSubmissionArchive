import sys
from copy import deepcopy
from random import randint
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
inv value is the number of subsegments containing inversions
must be in range n-1 to n(n-1)/2+1-n, unless it's 2 or 3, those cases
are brute force
random bs machine go
"""

#for _ in range(readint()):
#    n,k = readints()

def f(ar):
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]: return True
    return False

def invcount(n,ar):
    ans = 0
    for a in range(n-1):
        for b in range(a+1,n):
            if f(ar[a:b+1]):
                ans += n-b
                break
    return ans

n = 30
ar = [i for i in range(1,n+1)]

s = 0
d = [0]*436 # middle is 217
for k in range(1,21):
    for _ in range(1050-k*50):
        br = deepcopy(ar)
        for _ in range(k):
            a = randint(0,n-1)
            b = randint(0,n-1)
            br[a],br[b] = br[b],br[a]
        x = invcount(n,br)
        s += x
        d[x] += 1
