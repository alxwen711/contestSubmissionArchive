import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,m = readints()
    a = input()
    b = input()
    c = a+b[::-1]
    d = 0
    for j in range(n+m-1):
        if c[j] == c[j+1]: d += 1
    if d > 1: print("NO")
    else: print("YES")
