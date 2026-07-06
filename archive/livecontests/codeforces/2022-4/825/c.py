import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    m = 1
    ans = 0
    for j in range(n):
        if ar[j] >= m:
            ans += m
            m += 1
        else:
            ans += ar[j]
            m = ar[j]+1
    print(ans)
