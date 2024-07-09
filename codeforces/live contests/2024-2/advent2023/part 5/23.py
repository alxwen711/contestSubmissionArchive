from copy import deepcopy
ar = list()
#input, default to basic integer reading file
f = open("23.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

print(len(ar),len(ar[0]),len(ar[-1]))


"""
some sort of graph search
there is ONLY > and v
set E points at start, end and anywhere with 3 arrows
no choice split paths ...
                       .
thus can create graph between E points
just create graph and brute force it, can't be that many nodes right?

part 2, there is a higher solution than 5994
do extremely limited binary search??
6010 is still too low, definitely missing a better path
higher than 6098

this is apparently brute forcable, idk why or how, but at this point, f it
"""

def fsearch(ar,br,p,ix,iy,points):
    sp = points[p] #get starting point id
    br[p[0]][p[1]] = 0
    px,py = p[0]+ix,p[1]+iy 
    br[px][py] = 1
    c = 1
    while True:
        if points.get((px,py)) != None:
            print("edge of length",c,"from node",sp,"to node",points[(px,py)])
            return sp,points[(px,py)],c
        elif ar[px][py] == ">":
            py += 1
        elif ar[px][py] == "v":
            px += 1
        elif ar[px][py] == "<":
            py -= 1
        elif ar[px][py] == "^":
            px -= 1
        else: #should be only one possible direction
            if ar[px-1][py] != "#" and br[px-1][py] == -1:
                px -= 1
            elif ar[px+1][py] != "#" and br[px+1][py] == -1:
                px += 1
            elif ar[px][py-1] != "#" and br[px][py-1] == -1:
                py -= 1
            elif ar[px][py+1] != "#" and br[px][py+1] == -1:
                py += 1
            else: break
        c += 1
        br[px][py] = c
    print("error occurred with search from point",p)
    print(ix,iy,"are directions attempted")
    return


class Node:
    def __init__(self):
        self.edges = {}
        
n = len(ar)

br = list()
for _ in range(n):
    tmp = [-1]*n
    br.append(tmp)
    
points = {}
points[(0,1)] = 0
nc = 1
pp = list()
pp.append((0,1))
for a in range(1,n-1):
    for b in range(1,n-1):
        arrows = 0
        if ar[a-1][b] != "." and ar[a-1][b] != "#": arrows += 1
        if ar[a+1][b] != "." and ar[a+1][b] != "#": arrows += 1
        if ar[a][b-1] != "." and ar[a][b-1] != "#": arrows += 1
        if ar[a][b+1] != "." and ar[a][b+1] != "#": arrows += 1
        if arrows >= 3:
            points[(a,b)] = nc
            nc += 1
            pp.append((a,b))

points[(n-1,n-2)] = nc

print(nc, "label from 0")
nodes = list()
for _ in range(36):
    nodes.append(Node())
for i in range(nc):
    if i == 0: #only search downwards
        na,nb,cost = fsearch(ar,deepcopy(br),pp[i],1,0,points)
        nodes[na].edges[nb] = cost
        nodes[nb].edges[na] = cost
    else:
        xx,yy = pp[i][0],pp[i][1]
        if ar[xx+1][yy] == "v":
            na,nb,cost = fsearch(ar,deepcopy(br),pp[i],1,0,points)
            nodes[na].edges[nb] = cost
            nodes[nb].edges[na] = cost
        if ar[xx][yy+1] == ">":
            na,nb,cost = fsearch(ar,deepcopy(br),pp[i],0,1,points)
            nodes[na].edges[nb] = cost
            nodes[nb].edges[na] = cost
q = [(0,0,{0:1})]
ans = 0
while len(q) != 0:
    x = q.pop()
    nv = x[0]
    cost = x[1]
    dd = x[2]
    if nv == 35:
        if cost > ans:
            ans = cost
            print(ans)
    else:
        for ii in nodes[nv].edges.keys():
            if dd.get(ii) == None:
                #clone dict
                d = {}
                for snth in dd.keys():
                    d[snth] = 1
                d[ii] = 1
                q.append((ii,cost+nodes[nv].edges[ii],d))
print("final ans:",ans)
