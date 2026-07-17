import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


for _ in range(readint()):
    n = readint()
    ar = [0]*n
    for i in range(n-1):
        a,b = readints()
        a -= 1
        b -= 1
        ar[a] += 1
        ar[b] += 1
    one = ar.count(1)
    if one == 1: print(0)
    elif one == 2: print(1)
    elif one == 3: print(2)
    elif one == 4: print(2)
    else: print((one+1)//2)
