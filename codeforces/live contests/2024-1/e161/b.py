import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    ar = readar()
    h = [0]*(n+1)
    for i in ar:
        h[i] += 1
    ans = 0
    for e in h:
        if e >= 3:
            ans += ((e)*(e-1)*(e-2))//6
    count = 0
    for j in range(n):
        count += h[j]
        if h[j+1] >= 2:
            ans += (h[j+1]*(h[j+1]-1))//2*count
    print(ans)
