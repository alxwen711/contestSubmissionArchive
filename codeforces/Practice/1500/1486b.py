import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
summary distance means only sum of ALL distances is minimized, not
maximum distance for a given house


find the middle point in x/y co-ords, if two houses, can vary in that range
"""
for i in range(readint()):
    n = readint()
    ar = list()
    br = list()
    for j in range(n):
        a,b = readints()
        ar.append(a)
        br.append(b)
    ar.sort()
    br.sort()
    if n % 2 == 1: print(1) #odd number will have only 1 pt?
    else: print((ar[n//2]-ar[n//2-1]+1)*(br[n//2]-br[n//2-1]+1))
