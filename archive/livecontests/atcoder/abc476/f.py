import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
radius distance is in use
there are ai * bi mod M people in each cell
some sort of efficient method to determining the
radial sum cost is needed

using prefix sums there can only be up to distance 1500 (n x n grid)

that would be O(n^3), O(n^2) needed

maybe a way to do extend prefix sums to extreme case

lrd = bottom left to top right diagonals, id is topleft->botleft->botright
rld = top left to bot right diagonals, id is botleft->topleft->topright
trapezoids should include the center? but that's 0
"""

def init_grid(n):
    ar = list()
    for _ in range(n):
        tmp = [0]*n
        ar.append(tmp)
    return ar

def valid(x,y,n):
    if x < 0: return False
    if y < 0: return False
    if x >= n: return False
    if y >= n: return False
    return True

def diagonal_compute(n,grid,starts,dx,dy):
    ar = list()
    for s in starts:
        tmp = [0]
        px,py = s[0],s[1]
        while valid(px,py,n):
            tmp.append(tmp[-1]+grid[px][py])
            px += dx
            py += dy
        ar.append(tmp)
    return ar


def lrd_compute(grid,lrd,a,b,c,d):
    if a < c: return lrd_compute(grid,lrd,c,d,a,b)
    if a == c: return grid[a][b]
    n = len(grid)
    # either y is 0 or x is n-1
    dist = min(n-a-1,b)
    sx,sy = a+dist,b-dist
    iv = -1
    if sy == 0:
        iv = sx
        return lrd[iv][d+1]-lrd[iv][b]
    else:
        iv = n-1+sy
        return lrd[iv][n-c]-lrd[iv][n-a-1]
        
    

def rld_compute(grid,rld,a,b,c,d):
    if a > c: return rld_compute(grid,rld,c,d,a,b)
    if a == c: return grid[a][b]
    n = len(grid)
    # either y is 0 or x is n-1
    dist = min(a,b)
    sx,sy = a-dist,b-dist
    iv = -1
    if sy == 0:
        iv = n-sx-1
        return rld[iv][d+1]-rld[iv][b]
    else:
        iv = n-1+sy
        return rld[iv][c+1]-lrd[iv][a]

n,m = readints()
ar = readar()
br = readar()
grid = list()
for i in range(n):
    tmp = list()
    for j in range(n):
        tmp.append((ar[i]*br[j]) % m)
    grid.append(tmp)


lrd_starts = list()
for i in range(n):
    lrd_starts.append((i,0))
for i in range(1,n):
    lrd_starts.append((n-1,i))


rld_starts = list()
for i in range(n-1,-1,-1):
    rld_starts.append((i,0))
for i in range(1,n):
    rld_starts.append((0,i))

lrd = diagonal_compute(n,grid,lrd_starts,-1,1)
rld = diagonal_compute(n,grid,rld_starts,1,1)

# top left diagonal
tld = init_grid(n)
for i in range(1,n):
    sx,sy = 1,i
    v = 0
    while sx < n and sy < n:
        v += grid[sx-1][sy-1]
        tld[sx][sy] = tld[sx-1][sy-1]+v 
        sx += 1
        sy += 1
        
for i in range(2,n):
    sx,sy = i,1
    v = 0
    while sx < n and sy < n:
        v += grid[sx-1][sy-1]
        tld[sx][sy] = tld[sx-1][sy-1]+v 
        sx += 1
        sy += 1

# top right diagonal
trd = init_grid(n)
for i in range(n-1):
    sx,sy = 1,i
    v = 0
    while sx < n and sy >= 0:
        v += grid[sx-1][sy+1]
        trd[sx][sy] = trd[sx-1][sy+1]+v 
        sx += 1
        sy -= 1
        
for i in range(2,n):
    sx,sy = i,n-1
    v = 0
    while sx < n and sy >= 0:
        v += grid[sx-1][sy+1]
        trd[sx][sy] = trd[sx-1][sy+1]+v 
        sx += 1
        sy -= 1


# bot left diagonal
bld = init_grid(n)
for i in range(1,n):
    sx,sy = n-2,i
    v = 0
    while sx >= 0 and sy < n:
        v += grid[sx+1][sy-1]
        bld[sx][sy] = bld[sx+1][sy-1]+v 
        sx -= 1
        sy += 1
        
for i in range(n-2):
    sx,sy = i,1
    v = 0
    while sx >= 0 and sy < n:
        v += grid[sx+1][sy-1]
        bld[sx][sy] = bld[sx+1][sy-1]+v 
        sx -= 1
        sy += 1
    
# bot right diagonal
brd = init_grid(n)
for i in range(n-1):
    sx,sy = n-2,i
    v = 0
    while sx >= 0 and sy >= 0:
        v += grid[sx+1][sy+1]
        bld[sx][sy] = bld[sx+1][sy+1]+v 
        sx -= 1
        sy -= 1
        
for i in range(n-2):
    sx,sy = i,n-2
    v = 0
    while sx >= 0 and sy >= 0:
        v += grid[sx+1][sy+1]
        bld[sx][sy] = bld[sx+1][sy+1]+v 
        sx -= 1
        sy -= 1


# up cases
up = init_grid(n)
for b in range(n):
    v = 0
    for a in range(1,n):
        v += grid[a-1][b]
        sx,sy = a-1,b-1
        if valid(sx,sy,n):
            dist = min(sx,sy)
            v += rld_compute(grid,rld,sx-dist,sy-dist,sx,sy)
        sx,sy = a-1,b+1
        if valid(sx,sy,n):
            dist = min(sx,n-sy-1)
            v += lrd_compute(grid,lrd,sx-dist,sy+dist,sx,sy)
        up[a][b] = up[a-1][b]+v
        
# down cases
down = init_grid(n)
for b in range(n):
    v = 0
    for a in range(n-2,-1,-1):
        v += grid[a+1][b]
        sx,sy = a+1,b-1
        if valid(sx,sy,n):
            dist = min(n-sx-1,sy)
            v += lrd_compute(grid,lrd,sx+dist,sy-dist,sx,sy)
        sx,sy = a+1,b+1
        if valid(sx,sy,n):
            dist = min(n-sx-1,n-sy-1)
            v += rld_compute(grid,rld,sx+dist,sy+dist,sx,sy)
        down[a][b] = down[a+1][b]+v

# left cases
left = init_grid(n)
for a in range(n):
    v = 0
    for b in range(1,n):
        v += grid[a][b-1]
        sx,sy = a-1,b-1
        if valid(sx,sy,n):
            dist = min(sx,sy)
            v += rld_compute(grid,rld,sx-dist,sy-dist,sx,sy)
        sx,sy = a+1,b-1
        if valid(sx,sy,n):
            dist = min(n-sx-1,sy)
            v += lrd_compute(grid,lrd,sx+dist,sy-dist,sx,sy)
        left[a][b] = left[a][b-1]+v

# right cases
right = init_grid(n)
for a in range(n):
    v = 0
    for b in range(n-2,-1,-1):
        v += grid[a][b+1]
        sx,sy = a-1,b+1
        if valid(sx,sy,n):
            dist = min(sx,n-sy-1)
            v += lrd_compute(grid,lrd,sx-dist,sy+dist,sx,sy)
        sx,sy = a+1,b+1
        if valid(sx,sy,n):
            dist = min(n-sx-1,n-sy-1)
            v += rld_compute(grid,rld,sx+dist,sy+dist,sx,sy)
        down[a][b] = down[a][b+1]+v

# answers

ans = 0
for a in range(n):
    for b in range(n):
        v = up[a][b]+down[a][b]+left[a][b]+right[a][b]-tld[a][b]-trd[a][b]-bld[a][b]-brd[a][b]
        v = a*n+b+v
        ans ^= v
print(ans)







    


