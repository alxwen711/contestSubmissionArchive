import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    s = sum(ar)
    if s % 2 == 0: print(0)
    else:
        best = 9999999
        for j in range(len(ar)):
            x = ar[j]
            it = 0
            while True:
                it += 1
                x = x // 2
                if (ar[j]-x) % 2 == 1: break
            best = min(it,best)
        print(best)
