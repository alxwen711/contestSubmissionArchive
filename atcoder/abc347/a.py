import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,k = readints()
ar = readar()
ans = list()
for i in ar:
    if i % k == 0: ans.append(i//k)
print(*ans)
