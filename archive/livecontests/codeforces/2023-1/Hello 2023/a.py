import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    x = input()
    a,b = -1,999999999
    for j in range(n):
        if x[j] == "R":
            b = min(b,j+1)
        if x[j] == "L":
            a = max(a,j+1)
    if b == 999999999 or a == -1: print(-1)
    elif a > b: print(0)
    elif a+1 == b: print(a)
    else: print(-1)
