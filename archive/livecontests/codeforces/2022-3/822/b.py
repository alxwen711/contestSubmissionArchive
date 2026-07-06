import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    if n >= 1: print(1)
    if n >= 2: print("1 1")
    if n >= 3:
        ar = list()
        ar.append(1)
        ar.append(1)
        for j in range(n-2):
            ar.append(1)
            ar[-2] = 0
            print(*ar)
        
