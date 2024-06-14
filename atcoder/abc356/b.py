import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = readar()
for _ in range(n):
    br = readar()
    for i in range(m):
        ar[i] -= br[i]
if max(ar) > 0: print("No")
else: print("Yes")
