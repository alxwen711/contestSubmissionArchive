import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
empty 3x3 can be coloured in 4 times
2d bin search table
note n is at most 500, can do this more easily
"""

n,q = readints()
grid = list()
for _ in range(n):
    grid.append(readin())
base = list()
for i in range(n-1):
    tmp = list()
    for j in range(n-1):
        if grid[i][j] == "." and grid[i+1][j] == "." and grid[i][j+1] == "." and grid[i+1][j+1] == ".":
            tmp.append(1)
        else: tmp.append(0)
    base.append(tmp)

prefix = list()
for row in base:
    tmp = [0]
    for c in row:
        tmp.append(tmp[-1]+c)
    prefix.append(tmp)

for _ in range(q):
    a,b,c,d = readints()
    if c == d: print(0)
    else:
        ans = 0
        st,ed = c-1,d-1
        for k in range(a-1,b-1):
            ans += prefix[k][ed]-prefix[k][st]
        print(ans)
