import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = readar()
    ans = [0]*n
    for j in range(n):
        ans[j%k] = max(ans[j%k],ar[j])
    print(sum(ans))
