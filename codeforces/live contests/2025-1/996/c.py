import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
this is basically sudoku solver
sum up every row/col to 0

n,m go up to 1000, this CANNOT be hash broken
"""

def hv(a,b):
    #a,b = t[0],t[1]
    return (a*1234+b)^9277489189-69

for _ in range(readint()):
    n,m = readints()
    s = readin()
    grid = list()
    for _ in range(n):
        tmp = readar()
        grid.append(tmp)
    pts = [(0,0)]
    rpts = {}
    rpts[0] = [0]
    cpts = {}
    cpts[0] = [0]
    row = [0]*n
    col = [0]*m
    row[0] += 1
    col[0] += 1
    for i in s:
        if i == "D": pts.append((pts[-1][0]+1,pts[-1][1]))
        else: pts.append((pts[-1][0],pts[-1][1]+1))
        row[pts[-1][0]] += 1
        col[pts[-1][1]] += 1
        if rpts.get(pts[-1][0]) == None: rpts[pts[-1][0]] = list()
        rpts[pts[-1][0]].append(pts[-1][1])
        if cpts.get(pts[-1][1]) == None: cpts[pts[-1][1]] = list()
        cpts[pts[-1][1]].append(pts[-1][0])
    q = list()
    for j in range(n):
        if row[j] == 1: q.append((j,0))
    for k in range(m):
        if col[k] == 1: q.append((k,1))

    #print(row,col)
    #print(rpts,cpts)
    used = {}
    while len(q) != 0:
        x = q.pop()
        index = x[0]
        v = 0
        if x[1] == 0: # add row
            for l in range(m):
                v += grid[index][l]
            # determine point to use
            for r in rpts[index]:
                dv = hv(index,r)
                if used.get(dv) == None:
                    grid[index][r] = -v
                    used[dv] = 1
                    row[index] -= 1
                    col[r] -= 1
                    if col[r] == 1: q.append((r,1))
                    break
        else: # add col
            for l in range(n):
                v += grid[l][index]
            # determine point to use
            for r in cpts[index]:
                dv = hv(r,index)
                if used.get(dv) == None:
                    grid[r][index] = -v
                    used[dv] = 1
                    col[index] -= 1
                    row[r] -= 1
                    if row[r] == 1: q.append((r,0))
                    break
    for snth in grid:
        print(*snth)


                
