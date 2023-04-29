import sys
#from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
-7 -7 3 3 3

"""

def solve(n,ar):
    s = 0
    for i in range(n-1):
        if i % 2 == 0:
            s += (ar[i+1]-ar[i])
    return s < 0

for i in range(readint()):
    n = readint()
    ar = readar()
    if n % 2 == 1: print("YES")
    else:
        x = solve(n,ar)
        if not x:print("YES")
        else: print("NO")
