import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
add task to bfs queue once it has no more dependencies attached to it
calc separtely for each tree, then merge longest time to shortest time
do the task searching in reverse, finding minimum number of prep days
needed

WA test 3, failing on a significantly sized tree, not a low n value

some of the endpts could be a day earlier, combine previous idea

total tree time is the earlist latest start to the latest earliest finish
"""

class queue:
    def __init__(self,limit=100000):
        self.q = list()
        self.pt = 0
        self.l = 0
        self.memRefresh = limit

    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        #check if memory needs to be refreshed
        if self.pt == self.memRefresh:
            self.pt = 0
            self.l -= self.memRefresh
            self.q = self.q[self.memRefresh:]
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self) -> int:
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l


class Node:
    def __init__(self,ID,v):
        self.ID = ID
        self.v = v
        self.pc = 0
        self.cc = 0
        self.children = list()
        self.parents = list()
        self.ef = -1 #earliest finish
        self.ls = -1 #latest start

def bfs(n,nodes,x):
    d = {}
    d[x] = 1
    ar = [x]
    while len(ar) != 0:
        nod = ar.pop()
        nodey = nodes[nod]
        for i in nodey.children:
            if d.get(i) == None:
                d[i] = 1
                ar.append(i)
        for j in nodey.parents:
            if d.get(j) == None:
                d[j] = 1
                ar.append(j)
    return list(d.keys())

def treeset(n,m,k,nodes):
    h = [1]*n
    ans = list()
    for i in range(n):
        if nodes[i].pc == 0 and h[i] == 1: #new head, compute
            # first find ALL heads of this tree (using bfs/dfs)
            cr = bfs(n,nodes,i)
            q = queue()
            q2 = queue()
            for e in cr:
                if nodes[e].pc == 0:
                    q.add(e)
                if nodes[e].cc == 0:
                    q2.add(e)

            #compute earlist finish times
            while not q.empty():
                # update individual node
                x = q.dequeue()
                nd = nodes[x]
                h[x] = 0
                nd.ef = max(nd.ef,nd.v)
                #update next nodes
                for c in nodes[x].children:
                    inc = nodes[c].v-nd.v #if same day
                    if inc < 0: #must go to next day
                        inc += k
                    nodes[c].ef = max(nodes[c].ef,nd.ef+inc) 
                    nodes[c].pc -= 1
                    if nodes[c].pc == 0: #all prereqs done
                        q.add(c)

            #compute latest start times
            while not q2.empty():
                # update individual node
                x = q2.dequeue()
                nd = nodes[x]
                h[x] = 0
                nd.ls = max(nd.ef,nd.ls)
                #update next nodes
                for ccc in nodes[x].parents:
                    dec = nd.v-nodes[ccc].v #if same day
                    if dec < 0: #must go to next day
                        dec += k
                    nodes[ccc].ls = max(nodes[ccc].ls,nd.ls-dec) 
                    nodes[ccc].cc -= 1
                    if nodes[ccc].cc == 0: #all prereqs done
                        q2.add(ccc)
            #get st/ed pts
            st = 589734895743895345454543
            ed = -1
            for nth in cr:
                st = min(st,nodes[nth].ls)
                ed = max(ed,nodes[nth].ef)
            ans.append((st,ed))
    return ans
    
for i in range(readint()):
    n,m,k = readints()
    ar = readar()
    nodes = list()
    for j in range(n):
        nodes.append(Node(j,ar[j]))
    for o in range(m):
        a,b = readints()
        a -= 1
        b -= 1
        nodes[a].children.append(b)
        nodes[a].cc += 1
        nodes[b].parents.append(a)
        nodes[b].pc += 1        
    br = treeset(n,m,k,nodes)
    #print(br)
    br.sort()
    # merge tree times, very sure this part is correct
    fs = br[0][0]
    fe = -1
    for snth in br:
        fe = max(fe,snth[1])
    ans = fe-fs
    for c in range(len(br)-1):
        fs = br[c+1][0]
        fe = max(fe,br[c][1]+k)
        ans = min(ans,fe-fs)
    print(ans)
