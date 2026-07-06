import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
cycle has to begin with a split, could attempt by solving with each node
"""
class Node:
    def __init__(self,ID):
        self.ID = ID
        self.deg = 0
        self.parent = -1
        self.ancestor = -1
        self.depth = 0
        self.connected = list()

    def add(self,x):
        self.connected.append(x)
        self.deg += 1

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

def solve(n,m):
    aar = list()
    bbr = list()
    nodes = list()
    for snth in range(n+1):
        nodes.append(Node(snth))
    for j in range(m):
        a,b = readints()
        nodes[a].add(b)
        nodes[b].add(a)
        aar.append(a)
        bbr.append(b)
    #origin = -1
    for k in range(n+1):
        if nodes[k].deg >= 4: #possible origin
            origin = k
            #nodes[origin].parent = origin
            q = queue()
            q.add(origin)
            while not q.empty():
                x = q.dequeue()
                for l in nodes[x].connected:
                    if nodes[l].parent == -1:
                        nodes[l].parent = x
                        nodes[l].depth = nodes[x].depth+1
                        if nodes[l].depth == 1: nodes[l].ancestor = l
                        elif nodes[l].depth == 2: nodes[l].ancestor = x
                        elif nodes[l].depth > 2: nodes[l].ancestor = nodes[x].ancestor
                        q.add(l)
                    elif nodes[x].parent != l and nodes[l].ancestor != nodes[x].ancestor: 
                        ar = [x]
                        br = [l]
                        bnode = l
                        anode = x
                        while anode != origin:
                            anode = nodes[anode].parent
                            ar.append(anode)
                        while bnode != origin:
                            bnode = nodes[bnode].parent
                            br.append(bnode)
                        ar.reverse()
                        cr = ar+br
                        ea,eb = cr[1],cr[-2]
                        if ea != eb: #something is bugged with prev elif
                            print("YES")
                            dr = list()
                            for u in nodes[origin].connected:
                                if u != ea and u != eb: dr.append(u)
                            print(2+len(cr)-1)
                            print(dr[0],origin)
                            print(dr[1],origin)
                            for thn in range(len(cr)-1):
                                print(cr[thn],cr[thn+1])
                            return
            # node failed, reset graph
            nodes = list()
            for snth2 in range(n+1):
                nodes.append(Node(snth2))
            for jj in range(m):
                a,b = aar[jj],bbr[jj]
                nodes[a].add(b)
                nodes[b].add(a)
    
    
    print("NO") # no sol found
        
        

for i in range(readint()):
    n,m = readints()
    solve(n,m)
