import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,x,y = readints()
    n -= 1
    if x == 0 and y == 0: print(-1)
    elif x == 0 or y == 0:
        a = max(x,y)
        if n % a != 0: print(-1)
        else:
            ar = [0]*n
            v = 1
            for j in range(n//a):
                for k in range(a):
                    ar[j*a+k] = v
                if j == 0: v += 1
                v += a
            print(*ar)
    else: print(-1)
