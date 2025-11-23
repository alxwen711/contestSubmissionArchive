import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
either its a staircase, or 2x2 square exception
"""

for _ in range(readint()):
    n = readint()
    grid = list()
    pts = list()
    for i in range(n):
        grid.append(readin())
        for j in range(n):
            if grid[i][j] == "#": pts.append((i,j))
    if len(pts) == 0: print("YES")
    else:
        ans = "NO"
        # diagonal tests
        ar = list()
        for i in pts:
            ar.append(i[0]+i[1])
        ar.sort()
        if ar[-1]-ar[0] <= 1: ans = "YES"
        ar = list()
        for i in pts:
            ar.append(i[0]-i[1])
        ar.sort()
        if ar[-1]-ar[0] <= 1: ans = "YES"
        if len(pts) == 4: # square exception
            pts.sort()
            a,b = pts[0][0],pts[0][1]
            if pts[1] == (a,b+1) and pts[2] == (a+1,b) and pts[3] == (a+1,b+1):
                ans = "YES"
        print(ans)
