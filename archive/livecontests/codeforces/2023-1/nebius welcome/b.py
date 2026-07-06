import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k,d,w = readints()
    ar = readar()
    ans = 0
    enddate = 0
    doses = 0
    for j in range(n):
        x = ar[j]
        if x > enddate or doses == 0:
            ans += 1
            enddate = x+w+d
            doses = k-1
        else: doses -= 1
    print(ans)
    
