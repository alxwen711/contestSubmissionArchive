import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,k = readints()
ar = readar()

v = k
ans = 1
for i in ar:
    if i > v:
        ans += 1
        v = k
    v -= i
print(ans)
