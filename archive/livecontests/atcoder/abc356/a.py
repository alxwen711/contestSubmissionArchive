import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,l,r = readints()
ar = list()
for a in range(1,l):
    ar.append(a)
for i in range(r,l-1,-1):
    ar.append(i)
for j in range(r+1,n+1):
    ar.append(j)
print(*ar)
