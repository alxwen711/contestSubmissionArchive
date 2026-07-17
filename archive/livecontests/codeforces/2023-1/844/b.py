import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    g = False
    ans = 0
    for j in range(n):
        if ar[j] <= j:
            if not g:
                g = True
                ans += 1
        else:
            g = False
    if ar[0] > 0: ans += 1
    print(ans)
