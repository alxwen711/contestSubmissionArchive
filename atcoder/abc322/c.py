import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = readar()
ar.append(4389574893758943753475)
index = 0
for j in range(1,n+1):
    print(ar[index]-j)
    if ar[index] == j: index += 1
