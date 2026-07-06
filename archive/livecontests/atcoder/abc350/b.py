import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = [1]*(n+1)
ar[0] = 0
br = readar()
for i in br:
    ar[i] ^= 1
print(sum(ar))
