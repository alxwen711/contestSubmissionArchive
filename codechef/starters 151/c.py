import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
easy case has n = 1 (1d grid)
just consider each dimension seperately?
current method is only on manhattenn distance
have to refactor to fix such that maximum function is used
3's on this grid can be disregarded entirely
"""

for _ in range(readint()):
    n,m = readints()
    ar = list()
    for _ in range(n):
        ar.append(readar())
    fax = [0]*n # freq in each row
    fay = [0]*m # freq in each col
    fbx = [0]*n
    fby = [0]*m
    sax,say,sbx,sby = 0,0,0,0 # starting scores
    ashots,bshots = 0,0
    for x in range(n):
        for y in range(m):
            if ar[x][y] == 1 or ar[x][y] == 3: # A shot
                fax[x] += 1
                fay[y] += 1
                sax += x
                say += y
                ashots += 1
            if ar[x][y] == 2 or ar[x][y] == 3: # B shot
                fbx[x] += 1
                fby[y] += 1
                sbx += x
                sby += y
                bshots += 1
    print(sax,say,sbx,sby)
    # compute subans arrays
    ansax = list()
    d = ashots
    for i in range(n):
        ansax.append(sax)
        d -= (2*fax[i])
        sax -= d
    ansay = list()
    d = ashots
    for i in range(m):
        ansay.append(say)
        d -= 2*fay[i]
        say -= d
    ansbx = list()
    d = bshots
    for i in range(n):
        ansbx.append(sbx)
        d -= 2*fbx[i]
        sbx -= d
    ansby = list()
    d = bshots
    for i in range(m):
        ansby.append(sby)
        d -= 2*fby[i]
        sby -= d
    print(ansax,ansay,ansbx,ansby)
    for i in range(n):
        ans = list()
        for j in range(m):
            ans.append(abs(ansax[i]+ansay[j]-ansbx[i]-ansby[j]))
        print(*ans)
