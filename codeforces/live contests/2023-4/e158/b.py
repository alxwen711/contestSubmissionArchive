import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = ar[0]-1
    block = ar[0]
    for i in range(1,n):
        x = ar[i]
        if block >= x: block = x
        else:
            ans += (x-block)
            block = x
    print(ans)
    
