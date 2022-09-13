import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,m = readints()
    ar = readar()
    low = ar[0]
    high = ar[0]
    ans = 0
    for j in range(n):
        x = ar[j]
        if x > high: high = x
        if x < low: low = x
        if (high-low) > 2*m:
            low = x
            high = x
            ans += 1
    print(ans)
