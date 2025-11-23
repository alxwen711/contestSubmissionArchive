import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,m = readints()
ar = readar()

h = [0]*m
for i in ar:
    if i <= m: h[i-1] += 1
if min(h) == 0: print(0)
else:
    for j in range(n):
        if ar[-j-1] <= m:
            h[ar[-j-1]-1] -= 1
            if h[ar[-j-1]-1] == 0:
                print(j+1)
                break
