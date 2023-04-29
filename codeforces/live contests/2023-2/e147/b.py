import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
3 2 8 4
3 2 4 8
first diff and last diff have to start as endpoints
get min/max in those segments
extend to similar as far as possible
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    a,b = 9999999999999999,-1
    for j in range(n):
        if ar[j] != br[j]:
            a = min(a,j)
            b = max(b,j)
    l,h = br[a],br[b]
    while a != 0:
        if ar[a-1] <= l:
            l = ar[a-1]
            a -= 1
        else: break
    while b != n-1:
        if ar[b+1] >= h:
            h = br[b+1]
            b += 1
        else: break
    print(a+1,b+1)
