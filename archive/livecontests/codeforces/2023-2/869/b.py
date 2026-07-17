import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    if n == 1: print(1)
    elif n % 2 == 1: print(-1)
    else:
        ar = list()
        for j in range(n//2):
            ar.append(2*j+2)
            ar.append(2*j+1)
        print(*ar)
            
