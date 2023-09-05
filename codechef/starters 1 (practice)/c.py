import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# O(n log n) minimum

for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    a,b = ar[0],ar[1]
    c,d = ar[-1],ar[-2]
    e = a*b+abs(a-b)
    f = c*d+abs(c-d)
    print(max(e,f))
