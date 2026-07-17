import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
8 -> 4 5 6 7 9 10 11 12
7 -> 21 24 26 28 30 32 35
14**2 = 196
196/7 = 28
"""

for i in range(readint()):
    n = readint()
    ar = list()
    if n % 2 == 0:
        for j in range(n//2):
            ar.append(n-j-1)
            ar.append(n+j+1)
    else:
        x = n*4-(2*(n//2))
        for k in range(n):
            ar.append(x)
            x += 2
        ar[0] -= 1
        ar[-1] += 1
    print(*ar)
            
