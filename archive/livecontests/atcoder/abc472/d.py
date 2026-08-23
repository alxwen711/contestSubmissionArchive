import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

h,w,k = readints()
a = [1]*h
b = [1]*w
grid = list()

for i in range(h):
    s = readin()
    tmp = [0]*w
    grid.append(tmp)
    for j in range(w):
        if s[j] == "#":
            a[i] = 0
            b[j] = 0
            grid[i][j] = -1 # cannot move to bomb spots

q = list()

for x in range(h):
    for y in range(w):
        if grid[x][y] == 0:
            if a[x] == 1 and b[y] == 1:
                grid[x][y] = 0
                q.append((x,y))
            else:
                grid[x][y] = 9999999999

# then fill in the rest
ptr = 0
while ptr != len(q):
    xpos,ypos = q[ptr][0],q[ptr][1]
    v = grid[xpos][ypos]
    pspots = list()
    if xpos != 0:
        pspots.append((xpos-1,ypos))
    if xpos != h-1:
        pspots.append((xpos+1,ypos))
    if ypos != 0:
        pspots.append((xpos,ypos-1))
    if ypos != w-1:
        pspots.append((xpos,ypos+1))
    for pp in pspots:
        if grid[pp[0]][pp[1]] == 9999999999:
            grid[pp[0]][pp[1]] = v + 1
            q.append(pp)
    ptr += 1
    


ans = 0
for ii in range(h):
    for jj in range(w):
        if grid[ii][jj] != -1 and grid[ii][jj] <= k: ans += 1
print(ans)




    
