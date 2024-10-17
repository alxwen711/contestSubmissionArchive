import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
pretty much this is doing a 90 degree rotation clockwise
the layer level determines how many times it occurs
"""

n = readint()
grid = list()
for _ in range(n):
    s = readin()
    ar = list()
    for i in range(n):
        ar.append(s[i])
    grid.append(ar)

for i in range(n//2):
    for j in range((i+1)%4): # number of rotations
        for k in range(n-1-(2*i)):
            a,b = i,k+i
            grid[a][b],grid[b][n-a-1],grid[n-a-1][n-b-1],grid[n-b-1][a] = grid[n-b-1][a],grid[a][b],grid[b][n-a-1],grid[n-a-1][n-b-1]
for i in grid:
    print(*i,sep="")
