import sys
def solve(n,d):
    k = list(d.keys())
    h = [0]*n
    for a in range(len(k)):
        key = k[a]
        if len(d[key]) == 1:
            print(-1)
            return -1
        #len at least 2
        ll = len(d[key])
        for b in range(ll):
            h[d[key][(b+1)%ll]-1] = d[key][b]
    print(*h)
    return 0

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    d = {}
    for j in range(n):
        x = ar[j]
        if d.get(x) == None: d[x] = list()
        d[x].append(j+1)
    solve(n,d)
