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
q = list()
for i in range(h):
    s = readin()
    tmp = list()
    for j in range(w):
        if s[j] == "E":
            q.append((i,j))
        tmp.append(s[j])
    grid.append(tmp)

while len(q) != 0:
    nq = list()
    for i in q:
        a,b = i[0],i[1]
        if a != 0:
            if grid[a-1][b] == ".":
                grid[a-1][b] = "v"
                nq.append((a-1,b))
        if a != h-1:
            if grid[a+1][b] == ".":
                grid[a+1][b] = "^"
                nq.append((a+1,b))
        if b != 0:
            if grid[a][b-1] == ".":
                grid[a][b-1] = ">"
                nq.append((a,b-1))
        if b != w-1:
            if grid[a][b+1] == ".":
                grid[a][b+1] = "<"
                nq.append((a,b+1))
    q = nq
for snth in grid:
    print(*snth,sep="")
        
        
