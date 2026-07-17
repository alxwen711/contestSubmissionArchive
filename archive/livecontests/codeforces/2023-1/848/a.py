import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    x = sum(ar)
    b = 3
    for j in range(n-1):
        if (ar[j] + ar[j+1]) < b: b = (ar[j] + ar[j+1])
    x -= b
    x -= b
    print(x)
