import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
n,m = readints()
d = {}
for _ in range(m):
    a,b = readins()
    a = int(a)
    if b == "M":
        if d.get(a) == None:
            print("Yes")
            d[a] = 1
        else: print("No")
    else: print("No")
