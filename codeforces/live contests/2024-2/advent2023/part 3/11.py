ar = list()
#input, default to basic integer reading file
f = open("11.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
        
f.close()
def rc(a,b,ar):
    if a == b: return 0
    aindex = 0
    n = len(ar)
    while aindex != n:
        if ar[aindex] > a: break
        aindex += 1
    bindex = n-1
    while bindex != -1:
        if ar[bindex] < b: break
        bindex -= 1
    hits = bindex-aindex + 1
    return b-a-hits+(1000000*hits)
n,m = len(ar),len(ar[0])
rows = {}
cols = {}
br = list()
for _ in range(n):
    tmp = list()
    br.append(tmp)
for i in range(m):
    flag = True
    for j in range(n):
        if ar[j][i] == "#": flag = False
        br[j].append(ar[j][i])
    if flag: # empty
        cols[i] = 1
cr = list()
for a in range(len(ar)):
    cr.append(ar[a])
    if ar[a].count(".") == len(ar[a]): rows[a] = 1

dist = 1000000

pts = list()
xc = 0
yc = 0
for x in range(len(ar)):
    yc = 0
    if rows.get(x) == 1: xc += dist
    else:
        xc += 1
        for y in range(len(ar[x])):
            if cols.get(y) == 1: yc += dist
            else:
                yc += 1
                if ar[x][y] == "#": pts.append((xc,yc))
    
ans = 0
for g in range(len(pts)):
    for h in range(g,len(pts)):
        ans += abs(pts[g][0]-pts[h][0])
        ans += abs(pts[g][1]-pts[h][1])
print(ans)
