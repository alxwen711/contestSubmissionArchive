import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,x = readints()
    ar = readar()
    invalid = list()
    s = 0
    index = -1
    for i in range(n):
        s += ar[i]
        while s > x:
            index += 1
            invalid.append((i,index))
            s -= ar[index]
    invalid.sort()
    #print(invalid)
    h = [0]*n
    for a in invalid:
        h[a[0]] += 1
        if a[1] != 0:
            h[a[0]] += h[a[1]-1]
    print((n*n+n)//2-sum(h))
