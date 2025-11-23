import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if n is odd, spam singular value
if n is even
110
110
1000
1000

2 3 6 2 is impossible
11 100 101 110

any 2 is impossible
4 3 6 2 -> 3 3 4 4

if all values have the same leading bit, impossible
else set last two to whatever the next bit would be
"""

for _ in range(readint()):
    n,l,r,k = readints()
    if n % 2 == 1: print(l)
    elif n == 2: print(-1)
    else:
        base = 1
        while base <= l:
            base *= 2
        if base > r: print(-1)
        else:
            if k == n or k == n-1: print(base)
            else: print(l)
