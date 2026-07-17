import sys
for i in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    a = 2
    b = 2
    ar = list()
    tmp = list()
    tmp.append(1)
    tmp.append(0)
    ar.append(tmp)
    tmp = list()
    tmp.append(0)
    tmp.append(1)
    ar.append(tmp)
    while a < m:
        x = a
        for j in range(x):
            ar[0].append(ar[0][x-j-1])
            ar[1].append(ar[1][x-j-1])
        a = len(ar[0])
    while b < n:
        y = b
        for k in range(y):
            tmp = list()
            for l in range(a):
                tmp.append(ar[y-k-1][l])
            ar.append(tmp)
        b = len(ar)
    for f in range(n):
        print(*ar[f][:m])
            
            
