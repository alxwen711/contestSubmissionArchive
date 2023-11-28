import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    ar = readar()
    v = ar[-1]
    ans = 0
    for i in range(n-2,-1,-1):
        if ar[i] <= v: v = ar[i]
        else: #at least 1 division is needed
            inc = (ar[i]-1)//v
            ans += inc
            v = ar[i]//(inc+1)
    print(ans)
