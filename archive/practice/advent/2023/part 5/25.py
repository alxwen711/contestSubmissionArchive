class Node:
    def __init__(self):
        self.neighbours = list()

ar = list()
#input, default to basic integer reading file
f = open("25.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()


def valid(a,b,x,y,z):
    pa,pb = (a,b),(b,a)
    if pa == x or pb == x or pa == y or pb == y or pa == z or pb == z: return False
    return True

def countNodes(nodes,a,b,c,st,target):
    if st == a or st == b or st == c: return target #do not count
    d = {}
    q = [st]
    d[st] = 1
    ans = 1
    while len(q) != 0:
        x = q.pop()
        for i in nodes[x].neighbours:
            #if valid(x,i,a,b,c) and d.get(i) == None:
            if i != a and i != b and i != c and d.get(i) == None:
                ans += 1
                d[i] = 1
                q.append(i)
        if ans == target: break
    return ans

ans = 0
n = len(ar)
print(n,ar[0],ar[-1])

nodes = {}
edges = {}
el = list()
for i in range(n):
    h, br = ar[i].split(":")
    assert(len(h) == 3)
    br = list(map(str,br.split(" ")))
    if nodes.get(h) == None:
        nodes[h] = Node()
    for j in range(len(br)):
        x = br[j].lstrip().rstrip()
        if len(x) == 3:
            if nodes.get(x) == None:
                nodes[x] = Node()
            nodes[h].neighbours.append(x)
            nodes[x].neighbours.append(h)
            edges[(h,x)] = 1
            edges[(x,h)] = 1
            el.append((h,x))
print(len(el),"edges")
print(len(list(nodes.keys())),"nodes")

#i would think of something better, but I'm just about done, so brute force it is
#something FASTER than absolute brute force is needed (estimated 172 days)
#blacklist nodes with at most TWO edges (no way they can be the problem)
"""
10pm: currently the code is bricking through all the possible node shenanigan
setups, it can return a few potential answers (either full segment, 1 off, 2 off, or 3 off)
estimated to take about 7 days to finish XD

it's finally over, 514786 is the answer

now just 1 star remains.
"""
blacklist = {}
for ff in nodes.keys():
    if len(nodes[ff].neighbours) == 4: blacklist[ff] = 1

er = list()
for k in el:
    if blacklist.get(k[0]) == 1 and blacklist.get(k[1]) == 1:
        er.append(k)

en = len(er)
print(en,"reduced number of edges to search")
cr = list(nodes.keys())
nn = len(cr)
answer = -1
for a in range(nn-2):
    print(a,"a value out of",nn-2)
    for b in range(a+1,nn-1):
        #print(b)
        for c in range(b+1,nn):
            nf = countNodes(nodes,cr[a],cr[b],cr[c],"lrz",nn-3) # change to any starting node
            if nf != nn-3:
                print("FOUND ANSWER?")
                print("nodes found:",nf)
                print((nn-nf)*nf)
                answer = (nn-nf)*nf
