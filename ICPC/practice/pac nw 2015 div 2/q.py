import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

ar = list()
x = readint()
for i in range(x):
    n = readint()
    ar.append(n)
ar.sort()
ans = 89347689489643896349867
for j in range(x//2):
    ans = min(ans,ar[j]+ar[-j-1])
print(ans)
