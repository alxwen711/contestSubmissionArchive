import sys
from heapq import *
from copy import deepcopy
#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline()[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()


"""
there are at most 7**7 = 823k board states possible,
and most of these are straight up impossible
impossible if the count of burrows is incorrect
or if both players have a line
or if the placement of burrows literally cannot occur
this is bfs

if a scenario with a win is reached, stop searching that branch
"""

def checkwin(grid): # from partial completion, check if anyone won
    # hor wins
    for i in range(6):
        for j in range(4):
            if grid[i][j] == 1 and grid[i][j+1] == 1 and grid[i][j+2] == 1 and grid[i][j+3] == 1: return 1
            if grid[i][j] == 2 and grid[i][j+1] == 2 and grid[i][j+2] == 2 and grid[i][j+3] == 2: return 2
    # ver wins
    for i in range(3):
        for j in range(7):
            if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i+2][j] == 1 and grid[i+3][j] == 1: return 1
            if grid[i][j] == 2 and grid[i+1][j] == 2 and grid[i+2][j] == 2 and grid[i+3][j] == 2: return 2

    # diagonal wins
    for i in range(3):
        for j in range(4):
            if grid[i][j] == 1 and grid[i+1][j+1] == 1 and grid[i+2][j+2] == 1 and grid[i+3][j+3] == 1: return 1
            if grid[i][j] == 2 and grid[i+1][j+1] == 2 and grid[i+2][j+2] == 2 and grid[i+3][j+3] == 2: return 2
            if grid[i][j+3] == 1 and grid[i+1][j+2] == 1 and grid[i+2][j+1] == 1 and grid[i+3][j] == 1: return 1
            if grid[i][j+3] == 2 and grid[i+1][j+2] == 2 and grid[i+2][j+1] == 2 and grid[i+3][j] == 2: return 2
    
    return 0
# lines[x][y] = list of lines containing [x][y]

lines = list()
for _ in range(6):
    tmp = list()
    for _ in range(7):
        tmp2 = list()
        tmp.append(tmp2)
    lines.append(tmp)
# fill lines in
for i in range(6):
    for j in range(4):
        lv = [(i,j),(i,j+1),(i,j+2),(i,j+3)]
        for c in lv:
            lines[c[0]][c[1]].append(lv)
for i in range(3):
    for j in range(7):
        lv = [(i,j),(i+1,j),(i+2,j),(i+3,j)]
        for c in lv:
            lines[c[0]][c[1]].append(lv)
for i in range(3):
    for j in range(4):
        lv = [(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)]
        for c in lv:
            lines[c[0]][c[1]].append(lv)
        lv = [(i,j+3),(i+1,j+2),(i+2,j+1),(i+3,j)]
        for c in lv:
            lines[c[0]][c[1]].append(lv)

def checkwinsp(grid,x,y):
    for l in lines[x][y]:
        v = grid[l[0][0]][l[0][1]]
        if v != 0:
            flag = True
            for ii in range(1,4):
                if grid[l[ii][0]][l[ii][1]] != v:
                    flag = False
                    break
            if flag:
                return v
    return 0

def solve(grid): # actual solution goes here
    if checkwin(grid) == 0: return "0"
    h = [0]*(7**7) # avoid duplicate games
    h[0] = 1
    cwin = False
    fwin = False
    q = [(0,0,0,0)]
    while len(q) != 0:
        x = heappop(q)

        # gengrid based on x[1]
        hashes = list()
        tt = x[1]
        for _ in range(7):
            hashes.append(tt%7)
            tt //= 7
        gengrid = list()
        for i in range(6):
            tmp = list()
            for j in range(7):
                tmp.append(grid[i][j] if hashes[j]+i >= 6 else 0)
            gengrid.append(tmp)
        res = checkwinsp(gengrid,x[2],x[3])
        if res != 0:
            if res == 1: cwin = True
            else: fwin = True
            if cwin and fwin:
                return "?"
        else:
            m = 1
            if x[0] % 2 == 1: m = 2
            hv = x[1]
            tmpg = hv
            for i in range(7): # 1,7,49,343...
                ccr = tmpg % 7
                if ccr != 6:
                    if grid[-ccr-1][i] == m: # can make move here
                        nhv = hv+(7**i)
                        if h[nhv] == 0: # add new state
                            h[nhv] = 1
                            heappush(q,(x[0]+1,nhv,5-ccr,i))
                tmpg //= 7
    #print(sum(h))
    if cwin: return "C"
    return "F"
            
filename = "2b3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    print(i)
    # get input here
    readin()
    grid = list()
    for _ in range(6):
        tmp = list()
        for g in readin():
            if g == "C": tmp.append(1)
            else: tmp.append(2)
        grid.append(tmp)
    ans.append(solve(grid))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

