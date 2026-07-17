import sys
from itertools import permutations
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
6 6
2 2 2 2
-2 -1 -1 3

"""
def solve(n,ar):
    if n == 1: return abs(ar[1]-ar[0])

for i in range(readint()):
    n = readint()
    ar = readar()
    h = [0]*(n+1)
    h[0] = sum(ar[:n])
    for j in range(1,n+1):
        h[j] = h[j-1]+ar[j-1+n]-ar[j-1]
    #print(h)
    print(solve(n,ar))


