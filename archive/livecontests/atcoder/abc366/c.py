import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

c = 0
d = {}
for _ in range(readint()):
    ar = readar()
    if ar[0] == 1:
        x = ar[1]
        if d.get(x) == None or d.get(x) == 0:
            c += 1
            d[x] = 1
        else: d[x] += 1
    elif ar[0] == 2:
        x = ar[1]
        d[x] -= 1
        if d[x] == 0: c -= 1
    else:
        print(c)
