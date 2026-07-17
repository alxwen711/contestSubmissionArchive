import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = readar()
    h = [0]*k
    for j in range(k):
        if ar[j] <= k: h[ar[j]-1] += 1
    print (h.count(0))
