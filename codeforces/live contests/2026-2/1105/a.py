import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# sum must be under n

for _ in range(readint()):
    n,k = readints()
    ans = 0
    cost = 1
    while True:
        tc = cost*k
        if tc <= n:
            ans += k
            n -= tc
        else:
            ans += (n//cost)
            break
        cost *= 2
    print(ans)
        
