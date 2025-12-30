import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    a,b = readints()
    c,d = 0,0
    ans = 0
    while True:
        if ans % 2 == 0: c += 2**ans
        else: d += 2**ans
        if (a >= c and b >= d) or (b >= c and a >= d): ans += 1
        else: break
    print(ans)
    
