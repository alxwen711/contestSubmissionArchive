import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

h,w = readints()

grid = list()
for _ in range(h):
    tmp = ["."]*w
    grid.append(tmp)

for i in range(h):
    grid[i][0] = "#"
    grid[i][-1] = "#"

for j in range(w):
    grid[0][j] = "#"
    grid[-1][j] = "#"

for snth in grid:
    print(*snth,sep="")
