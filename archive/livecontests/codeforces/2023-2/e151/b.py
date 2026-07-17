import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a0,a1 = readints()
    b0,b1 = readints()
    c0,c1 = readints()
    bh = b0-a0
    bv = b1-a1
    ch = c0-a0
    cv = c1-a1
    ans = 1
    if bh*ch > 0: ans += min(abs(bh),abs(ch))
    if bv*cv > 0: ans += min(abs(bv),abs(cv))
    print(ans)
