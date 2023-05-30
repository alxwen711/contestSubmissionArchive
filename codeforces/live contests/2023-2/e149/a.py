import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    x,k = readints()
    if x % k == 0:
        print(2)
        print(-1,x+1)
    else:
        print(1)
        print(x)
