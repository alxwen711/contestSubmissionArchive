import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


for i in range(readint()):
    n = readint()
    if n == 1: print("1")
    elif n == 2: print("1 2")
    else:
        mark = n//2
        c = 4
        ar = [0]*n
        for j in range(n):
            if j != 0 and j != n-1 and j != mark:
                ar[j] = c
                c += 1
        ar[0] = 2
        ar[-1] = 3
        ar[mark] = 1
        print(*ar)
