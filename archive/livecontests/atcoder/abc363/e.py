import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
flood fill with entry points depending on requisite
"""

h,w,y = readints()
island = list()
hitable = list() # tiles that can be accessed
for _ in range(h):
    island.append(readar())
    tmp = [0]*w
    hitable.append(tmp)

for ss in range(h):
    hitable[ss][0] = 1
    hitable[ss][-1] = 1
    
for tt in range(w):
    hitable[0][tt] = 1
    hitable[-1][tt] = 1

d = {}
for i in range(h):
    for j in range(w):
        x = island[i][j]
        if d.get(x) == None: d[x] = list()
        d[x].append((i,j))

ans = h*w
for k in range(1,y+1):
    if d.get(k) != None:
        for p in d[k]:
            if hitable[p[0]][p[1]] == 1: # new sinkable
                hitable[p[0]][p[1]] = 2
                ans -= 1
                # dfs/bfs search
                q = [(p[0],p[1])]
                while len(q) != 0:
                    x = q.pop()
                    a,b = x[0],x[1]
                    if a != 0:
                        if hitable[a-1][b] != 2:
                            hitable[a-1][b] = 1
                            if island[a-1][b] <= k:
                                hitable[a-1][b] = 2
                                ans -= 1
                                q.append((a-1,b))
                    if a != h-1:
                        if hitable[a+1][b] != 2:
                            hitable[a+1][b] = 1
                            if island[a+1][b] <= k:
                                hitable[a+1][b] = 2
                                ans -= 1
                                q.append((a+1,b))
                    if b != 0:
                        if hitable[a][b-1] != 2:
                            hitable[a][b-1] = 1
                            if island[a][b-1] <= k:
                                hitable[a][b-1] = 2
                                ans -= 1
                                q.append((a,b-1))
                    if b != w-1:
                        if hitable[a][b+1] != 2:
                            hitable[a][b+1] = 1
                            if island[a][b+1] <= k:
                                hitable[a][b+1] = 2
                                ans -= 1
                                q.append((a,b+1))
    print(ans)
