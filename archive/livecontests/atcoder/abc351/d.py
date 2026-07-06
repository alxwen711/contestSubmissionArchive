import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
basic flood fill
"""

def adj(ar,h,w,a,b):
    if (a+1) != h:
        if ar[a+1][b] == "#": return True
    if (a-1) != -1:
        if ar[a-1][b] == "#": return True
    if (b+1) != w:
        if ar[a][b+1] == "#": return True
    if (b-1) != -1:
        if ar[a][b-1] == "#": return True
    return False

h,w = readints()
ar = list()
for _ in range(h):
    s = input()
    tmp = list()
    for i in range(w):
        tmp.append(s[i])
    ar.append(tmp)

ans = 0
for a in range(h):
    for b in range(w):
        if ar[a][b] == ".":
            if not adj(ar,h,w,a,b): #flood fill
                ar[a][b] = "o"
                spots = {}
                spots[(a,b)] = 1
                q = [(a,b)]
                subans = 1
                while len(q) != 0:
                    pos = q.pop()
                    x,y = pos[0],pos[1]
                    if (x+1) != h:
                        if ar[x+1][y] == "." and spots.get((x+1,y)) == None:
                            subans += 1
                            spots[(x+1,y)] = 1
                            if not adj(ar,h,w,x+1,y):
                                ar[x+1][y] = "o"
                                q.append((x+1,y))
                    if (x-1) != -1 and spots.get((x-1,y)) == None:
                        if ar[x-1][y] == ".":
                            subans += 1
                            spots[(x-1,y)] = 1
                            if not adj(ar,h,w,x-1,y):
                                ar[x-1][y] = "o"
                                q.append((x-1,y))
                    if (y+1) != w and spots.get((x,y+1)) == None:
                        if ar[x][y+1] == ".":
                            subans += 1
                            spots[(x,y+1)] = 1
                            if not adj(ar,h,w,x,y+1):
                                ar[x][y+1] = "o"
                                q.append((x,y+1))
                    if (y-1) != -1 and spots.get((x,y-1)) == None:
                        if ar[x][y-1] == ".":
                            subans += 1
                            spots[(x,y-1)] = 1
                            if not adj(ar,h,w,x,y-1):
                                ar[x][y-1] = "o"
                                q.append((x,y-1))
                ans = max(ans,subans)
            else: ans = max(ans,1)
print(ans)
