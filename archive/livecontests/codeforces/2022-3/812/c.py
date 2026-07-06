import sys
from math import sqrt
from math import ceil


#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
0
1 0
1 0 2
0 3 2 1
4 3 2 1 0
0 3 2 1 5 4
1 0 2 6 5 4 3
1 0 7 6 5 4 3 2
0 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1 0
0 3 2 1 5 4 A 9 8 7 6
"""

for i in range(readint()):
    n = readint()
    ar = [0]*n
    endpt = n
    val = n-1
    while val >= 0:
        x = ceil(sqrt(val)) ** 2
        st = x-val
        for j in range(st,endpt):
            ar[j] = val
            val -= 1
        endpt = st
    print(*ar)
        
