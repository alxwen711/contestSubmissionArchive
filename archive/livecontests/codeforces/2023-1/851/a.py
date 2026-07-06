import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    c = ar.count(2)
    if c % 2 == 0:
        a = c//2
        for j in range(n):
            if ar[j] == 2: a -= 1
            if a == 0:
                print(j+1)
                break
    else: print(-1)
