import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

moves = [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]

n,m = readints()
d = {}
for _ in range(m):
    x,y = readints()
    d[(x,y)] = 1
    for i in moves:
        a,b = x+i[0],y+i[1]
        if max(a,b) <= n and min(a,b) >= 1: d[(a,b)] = 1
print(n*n-len(list(d.keys())))
