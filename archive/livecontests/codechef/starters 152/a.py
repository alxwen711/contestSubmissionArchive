import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,m = readints()
    ar = list()
    for _ in range(m):
        ar.append(readin())
    ans = 0
    for i in range(n):
        a,b,q = 0,0,0
        for j in range(m):
            if ar[j][i] == "1": a += 1
            elif ar[j][i] == "0": b += 1
            else: q += 1
        for _ in range(q):
            if a > b: b += 1
            else: a += 1
        ans += a*b
    print(ans)
