import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 -> 1
2 -> 2 1
3 -> 1 3 2
4 -> 2 1 4 3
5 -> 1 3 2 5 4
6 -> 2 1 4 3 6 5
"""

for i in range(readint()):
    n = readint()
    ar = list()
    if n % 2 == 1:
        ar.append(1)
        for j in range(n//2):
            ar.append(2*j+3)
            ar.append(2*j+2)
    else:
        for k in range(n//2):
            ar.append(2*k+2)
            ar.append(2*k+1)
    print(*ar)
            
            

