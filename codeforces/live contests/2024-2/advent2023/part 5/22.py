ar = list()
#input, default to basic integer reading file
f = open("22.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

br = list()
height = 0
d = {}
for i in range(len(ar)):
    tmp = list(map(str,ar[i].split(",")))
    tmp2 = list(map(int,tmp[2].split("~")))
    tmp3 = [int(tmp[0]),int(tmp[1]),tmp2[0],tmp2[1],int(tmp[3]),int(tmp[4])]
    br.append(tmp3)
    height = max(height,tmp3[-1])
    if d.get(tmp3[2]) == None: d[tmp3[2]] = list()
    d[tmp3[2]].append(tmp3)
print(br[0])
print(height)
"""
[ax,ay,az,bx,by,bz], cube of point A to B opposing corners
z is the height value, everything is in a 10*10 x/y floor
start from the lowest z co-ordinate and walk upwards

then id check and track how many supports each brick has
anything with 1 support cannot be removed, everything else can

1203 total blocks
612 is wrong
721 is wrong

Part 2
124400 is wrong

i'm really coding n^2 for child detection, send help
"""

class Node:
    def __init__(self):
        self.supporting = list()
        self.degree = 0

def empty(ax,ay,bx,by,z,cr):
    for i in range(ax,bx+1):
        for j in range(ay,by+1):
            if cr[z][i][j] != 0: return False
    return True
    
cr = list() #[z][x][y]
for _ in range(300):
    tmp = list()
    for _ in range(10):
        tmp2 = [0]*10
        tmp.append(tmp2)
    cr.append(tmp)

index = 0
for h in range(300):
    if d.get(h) != None:
        for i in d[h]:
            index += 1
            ax,ay,az,bx,by,bz = i[0],i[1],i[2],i[3],i[4],i[5]           
            for a in range(az,bz+1):
                for b in range(ax,bx+1):
                    for c in range(ay,by+1):
                        cr[a][b][c] = index
            ceiling = bz
            base = az
            for e in range(base):
                az -= 1
                if empty(ax,ay,bx,by,az,cr): #move down 1
                    for xx in range(ax,bx+1):
                        for yy in range(ay,by+1):
                            cr[az][xx][yy] = index
                            cr[ceiling][xx][yy] = 0
                    ceiling -= 1
                else: break


#ans = [-1]*(len(br)+1) #-1, if support, track val, if supported and diff val, -2
ans = list()
for _ in range(len(br)+1):
    ddd = {}
    ans.append(ddd)
def generate(br):
    nodes = list()
    nn = len(br)
    for _ in range(nn-1):
        nodes.append(Node())
    for a in range(nn):
        for b in br[a].keys():
            #(a-1) supports (b-1)
            nodes[a-1].supporting.append(b-1)
            nodes[b-1].degree += 1
    return nodes
    
for r in range(299):
    for s in range(10):
        for t in range(10):
            if cr[r][s][t] != 0 and cr[r+1][s][t] != 0 and cr[r][s][t] != cr[r+1][s][t]:
                aa,bb = cr[r][s][t],cr[r+1][s][t]
                ans[aa][bb] = 1
                #if ans[bb] == -1: ans[bb] = aa
                #elif ans[bb] != aa: ans[bb] = -2
                
#print(ans.count(-1)+ans.count(-2))
#print(len(ans))
#print(ans)
#print(d)

"""
ans2 = [1]*len(br)
for kk in ans:
    if kk > 0:
        ans2[kk-1] = 0
print(sum(ans2))
#print(cr[:10])
"""
ans2 = 0
for ohno in range(len(ar)):
    t = generate(ans)
    ans3 = 0
    q = [ohno]
    while len(q) != 0:
        x = q.pop()
        for u in t[x].supporting:
            t[u].degree -= 1
            if t[u].degree == 0:
                ans3 += 1
                q.append(u)
    ans2 += ans3
    #if ans3 != 0: print(ohno,ans3)
print(ans2)
