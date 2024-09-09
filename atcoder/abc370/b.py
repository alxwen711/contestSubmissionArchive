import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = list()
for _ in range(n):
    br = readar()
    ar.append(br)

x = 1
for i in range(1,n+1):
    a = min(i,x)
    b = max(i,x)
    c = ar[b-1][a-1]
    x = c
print(x)
