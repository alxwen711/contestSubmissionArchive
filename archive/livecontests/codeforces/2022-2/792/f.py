import sys
for i in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    d = {}
    for j in range(n):
        x = ar[j]
        if d.get(x) == None:
            d[x] = list()
        d[x].append(j)
    print(d)
    for k in range(m):
        a,b = map(int,sys.stdin.readline().split())
