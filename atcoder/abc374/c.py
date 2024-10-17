import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = readar()
v = sum(ar)
best = v
for i in range(2**n):
    x = 0
    y = i
    for j in range(n):
        if y % 2 == 1: x += ar[j]
        y //= 2
    best = min(best,max(v-x,x))
print(best)
