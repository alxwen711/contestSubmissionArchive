import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if ? spot is adjacent to another ? spot, it can be made impossible
"""

def adjTest(es,x,y,n,m): # if ? is surrounded by exits, it is an exit
    if x != 0:
        if es[x-1][y] == 0: return False
    if x != n-1:
        if es[x+1][y] == 0: return False
    if y != 0:
        if es[x][y-1] == 0: return False
    if y != m-1:
        if es[x][y+1] == 0: return False
    return True

def solve(n,m,grid):
    if n == 1 and m == 1: return 0
    pts = list()
    es = list()
    for _ in range(n):
        tmp = [0]*m
        es.append(tmp)
    for i in range(m):
        if grid[0][i] == "U":
            pts.append((0,i))
            es[0][i] = 1 
        if grid[-1][i] == "D":
            pts.append((n-1,i))
            es[n-1][i] = 1
    for j in range(n):
        if grid[j][0] == "L":
            pts.append((j,0))
            es[j][0] = 1
        if grid[j][-1] == "R":
            pts.append((j,m-1))
            es[j][m-1] = 1

    # bfs/dfs search
    while len(pts) != 0:
        pt = pts.pop()
        x,y = pt[0],pt[1]
        # check up
        if x != 0:
            if es[x-1][y] == 0:
                if grid[x-1][y] == "D":
                    pts.append((x-1,y))
                    es[x-1][y] = 1
                elif grid[x-1][y] == "?":
                    if adjTest(es,x-1,y,n,m):
                        pts.append((x-1,y))
                        es[x-1][y] = 1
        if x != n-1:
            if es[x+1][y] == 0:
                if grid[x+1][y] == "U":
                    pts.append((x+1,y))
                    es[x+1][y] = 1
                elif grid[x+1][y] == "?":
                    if adjTest(es,x+1,y,n,m):
                        pts.append((x+1,y))
                        es[x+1][y] = 1
        if y != 0:
            if es[x][y-1] == 0:
                if grid[x][y-1] == "R":
                    pts.append((x,y-1))
                    es[x][y-1] = 1
                elif grid[x][y-1] == "?":
                    if adjTest(es,x,y-1,n,m):
                        pts.append((x,y-1))
                        es[x][y-1] = 1
        if y != m-1:
            if es[x][y+1] == 0:
                if grid[x][y+1] == "L":
                    pts.append((x,y+1))
                    es[x][y+1] = 1
                elif grid[x][y+1] == "?":
                    if adjTest(es,x,y+1,n,m):
                        pts.append((x,y+1))
                        es[x][y+1] = 1
        
    #print(es)
    # ans
    ans = n*m
    for ii in es:
        ans -= sum(ii)
    return ans
        
    
        
    

for _ in range(readint()):
    n,m = readints()
    grid = list()
    for _ in range(n):
        s = readin()
        ar = list()
        for i in s:
            ar.append(i)
        grid.append(ar)
    print(solve(n,m,grid))
    
