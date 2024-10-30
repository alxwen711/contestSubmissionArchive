import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

grid = list()
r = [1]*8
c = [1]*8
for i in range(8):
    s = readin()
    grid.append(s)
    for j in range(8):
        if s[j] == "#":
            r[i] = 0
            c[j] = 0
print(sum(r)*sum(c))
