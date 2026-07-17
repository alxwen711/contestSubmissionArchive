import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    no = list()
    mi,ma = -999999999999999999999999,99999999999999999999
    for _ in range(n):
        a,x = readints()
        if a == 1: mi = max(x,mi)
        elif a == 2: ma = min(x,ma)
        else: no.append(x)
    ans = ma-mi+1
    for e in no:
        if e >= mi and e <= ma: ans -= 1
    print(max(ans,0))
