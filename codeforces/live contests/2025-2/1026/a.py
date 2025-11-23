import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    if (ar[0]+ar[-1]) % 2 == 1:
        for i in range(n-1):
            if ar[0] % 2 != ar[i+1] % 2:
                print(i+1)
                break
            if ar[-1] % 2 != ar[-1-i-1] % 2:
                print(i+1)
                break
    else: print(0)
