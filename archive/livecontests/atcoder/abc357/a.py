import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = readar()

ans = 0
for i in ar:
    if i <= m:
        ans += 1
        m -= i
    else: break
print(ans)
