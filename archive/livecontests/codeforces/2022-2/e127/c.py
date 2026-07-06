import sys
for i in range(int(sys.stdin.readline())):
    n,x = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    ar.sort()
    s = list()
    rs = 0
    for j in range(n):
        rs += ar[j]
        s.append(rs)
    ans = 0
    for k in range(n):
        buy = x-s[k]
        if buy < 0: break
        r = buy
        buy = 1 + (r//(k+1))
        ans += buy
    print(ans)
