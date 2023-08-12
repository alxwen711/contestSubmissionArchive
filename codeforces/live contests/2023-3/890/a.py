import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    for j in range(n-1):
        if ar[j] > ar[j+1]:
            ans = max(ans,ar[j])
    print(ans)
