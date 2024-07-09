
def fs(ar):
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if ar[i][j] == "S": return i,j

def nv(c): #based on direction
    #print(c)
    #[u,d,l,r]
    if c == "|": return [1,1,0,0]
    elif c == "-": return [0,0,1,1]
    elif c == "L": return [1,0,0,1]
    elif c == "J": return [1,0,1,0]
    elif c == "7": return [0,1,1,0]
    elif c == "F": return [0,1,0,1]
    else: return [1,1,1,1]
    

# in between 352 and 736, try 480?
def loopfind(a,b,v,ar): #part 2 maybe make move list
    x,y = a,b
    move = v
    ml = [(y,x)]
    for i in range(20000):
        x += move[0]
        y += move[1]
        ml.append((y,x))
        if ar[y][x] == "S": return ml #end of loop
        br = nv(ar[y][x])
        if move == [-1,0]: br[3] ^= 1
        elif move == [1,0]: br[2] ^= 1
        elif move == [0,-1]: br[1] ^= 1
        else: br[0] ^= 1
        if sum(br) != 1:
            print(i)
            return -1 #something broke
        if br[0] == 1: move = [0,-1]
        elif br[1] == 1: move = [0,1]
        elif br[2] == 1: move = [-1,0]
        elif br[3] == 1: move = [1,0]
        
        

ar = list()

#input, default to basic integer reading file
f = open("10.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()
n,m = len(ar),len(ar[0])
print(n,m)


aar = list()
for sss in ar:
    tmp = list()
    for t in range(len(sss)):
        tmp.append(sss[t])
    aar.append(tmp)
ar = aar
br = ["|","-","L","J","7","F"]
yy,xx = fs(ar)
print(yy,xx)
print(ar[yy][xx])
ans = -1
for x in br:
    code = nv(x)
    if code[0] == 1:
        ans = loopfind(xx,yy,[0,-1],ar)
        if ans != -1:
            print(x)
            break
        
    if code[1] == 1:
        ans = loopfind(xx,yy,[0,1],ar)
        if ans != -1:
            print(x)
            break
        
    if code[2] == 1:
        ans = loopfind(xx,yy,[-1,0],ar)
        if ans != -1:
            print(x)
            break
        
    if code[3] == 1:
        ans = loopfind(xx,yy,[1,0],ar)
        if ans != -1:
            print(x)
            break
print(ans[1])

"""
for i in ans:
    ar[i[0]][i[1]] = " "
print(len(ans))

#dummy remove all outer cells
q = [(0,0)]
ar[0][0] = "0"
while len(q) != 0:
    xxx = q.pop()
    ax = xxx[0]
    ay = xxx[1]
    if ax != 0:
        if ar[ax-1][ay] != " " and ar[ax-1][ay] != "0":
            ar[ax-1][ay] = "0"
            q.append((ax-1,ay))
    if ax != 139:
        if ar[ax+1][ay] != " " and ar[ax+1][ay] != "0":
            ar[ax+1][ay] = "0"
            q.append((ax+1,ay))
    if ay != 0:
        if ar[ax][ay-1] != " " and ar[ax][ay-1] != "0":
            ar[ax][ay-1] = "0"
            q.append((ax,ay-1))
    if ay != 139:
        if ar[ax][ay+1] != " " and ar[ax][ay+1] != "0":
            ar[ax][ay+1] = "0"
            q.append((ax,ay+1))
    

f = open("10help.txt","w")
for aa in ar:
    for bb in aa:
        f.write(bb)
    f.write("\n")
f.close()
        
ans = 140*140
for iiii in ar:
    ans -= iiii.count(" ")
    ans -= iiii.count("0")


#answer is confirmed to be inbetween 352 and 480, can binary search on the system to the finish.
#update: bs got blocked, new plan is to blow up each spot into a 3*3 cell, then count the number of filled cells
#doing this tmr or when I have time because holy shit this is somehow a catastrophe
print(ans)
"""

def gen(x):
    if x == "|" or x == "S": return [[0,1,0],[0,1,0],[0,1,0]]
    if x == "-": return [[0,0,0],[1,1,1],[0,0,0]]
    if x == "L": return [[0,1,0],[0,1,1],[0,0,0]]
    if x == "J": return [[0,1,0],[1,1,0],[0,0,0]]
    if x == "7": return [[0,0,0],[1,1,0],[0,1,0]]
    if x == "F": return [[0,0,0],[0,1,1],[0,1,0]]
    if x == ".": return [[0,0,0],[0,0,0],[0,0,0]]
    
d = {}
for z in ans:
    d[z] = 1

dim = 420
dr = list()
for _ in range(420):
    tmp = list()
    dr.append(tmp)

for aa in range(140):
    for bb in range(140):
        template = [[0,0,0],[0,0,0],[0,0,0]]
        if d.get((aa,bb)) == 1:
            template = gen(ar[aa][bb])
        for cc in range(3):
            for dd in range(3):
                dr[3*aa+cc].append(template[cc][dd])

#fill in all outer cells
q = [(0,0)]
dr[0][0] = 2
while len(q) != 0:
    xxx = q.pop()
    ax = xxx[0]
    ay = xxx[1]
    if ax != 0:
        if dr[ax-1][ay] == 0:
            dr[ax-1][ay] = 2
            q.append((ax-1,ay))
    if ax != 419:
        if dr[ax+1][ay] == 0:
            dr[ax+1][ay] = 2
            q.append((ax+1,ay))
    if ay != 0:
        if dr[ax][ay-1] == 0:
            dr[ax][ay-1] = 2
            q.append((ax,ay-1))
    if ay != 419:
        if dr[ax][ay+1] == 0:
            dr[ax][ay+1] = 2
            q.append((ax,ay+1))

answer = 0
for xy in range(1,420,3):
    for yx in range(1,420,3):
        if dr[xy][yx] == 0: answer += 1
print(answer)
