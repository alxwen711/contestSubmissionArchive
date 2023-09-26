import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    flag = True
    a,b = readints()
    for j in range(n-1):
        c,d = readints()
        if c >= a and d >= b: flag = False
    print(a if flag else -1)
