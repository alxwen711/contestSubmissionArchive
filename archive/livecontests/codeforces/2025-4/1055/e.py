import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
perfect sequence will have n+1 skyscrapers on len n+1

n queries

could be increasing or decreasing
if every bit of the visible sequence is removed, eventually
we may reach a sequence?

if we don't, then last indices???

can attempt a directed acyclic graph construction, there's probably something that works
if we ever obtain a n+1 or longer sequence, then abort and output that
"""
class Node:
    def __init__(self):
        self.edges = {}
        self.deg = 0
        self.prev = -1
        self.chain = 1

def solution(nodes,m):
    print("solution from",m)
    for i in range(1,len(nodes)):
        print(i)
        print(nodes[i].deg,nodes[i].prev,nodes[i].chain)
        print()

def solve(n):
    h = [1]*(n*n+2)
    h[0] = 0
    nodes = ["why"]
    nodes2 = ["doublewhy"]
    lastchain = []
    for _ in range(n*n+1):
        nodes.append(Node())
        nodes2.append(Node())
    for _ in range(n):
        q = ["?",0]
        for i in range(1,n*n+2):
            if h[i] == 1:
                q.append(i)
                q[1] += 1
        s = " ".join(map(str,q))
        print(s)
        flush()
        ar = readar()
        if ar[0] >= n+1: # that's a solution
            ans = " ".join(map(str,ar[1:]))
            print("!",ans)
            flush()
            return

        
        # plug in the node setups
        nn = ar[0]
        ar = ar[1:]
        for a in range(nn-1):
            if nodes[ar[a]].edges.get(ar[a+1]) == None:
                nodes[ar[a]].edges[ar[a+1]] = 1
                nodes[ar[a+1]].deg += 1
            # nodes2 setups
            for b in range(ar[a]+1,ar[a+1]):
                if h[b] == 1:
                    for c in range(a+1):
                        if nodes2[b].edges.get(ar[c]) == None:
                            nodes2[b].edges[ar[c]] = 1
                            nodes2[ar[c]].deg += 1
            
        
        # for each node, link via lastchain
        for b in range(nn):
            h[ar[b]] = 0 # update for next query
            for c in lastchain:
                if ar[b] < c:
                    if nodes[ar[b]].edges.get(c) == None:
                        nodes[ar[b]].edges[c] = 1
                        nodes[c].deg += 1
                else:
                    if nodes2[c].edges.get(ar[b]) == None:
                        nodes2[c].edges[ar[b]] = 1
                        nodes2[ar[b]].deg += 1
            
        lastchain.append(ar[-1])
#        print(lastchain,h)
        for why in range(lastchain[-1]+1,len(h)):
            if h[why] == 1:
                if why < lastchain[-1]:
                    if nodes2[lastchain[-1]].edges.get(why) == None:
                        nodes2[lastchain[-1]].edges[why] = 1
                        nodes2[why].deg += 1
                #else:
                #    if nodes[lastchain[-1]].edges.get(why) == None:
                #        nodes[lastchain[-1]].edges[why] = 1
                #        nodes[why].deg += 1
                
        
    #for i in range(1,len(nodes)):
    #    print(i)
    #    print(nodes[i].edges.keys())
    #    print(nodes2[i].edges.keys())    
        
    if lastchain[-1] != n*n+1: # decreasing sequence found
        lastchain.append(n*n+1)
        ans = " ".join(map(str,lastchain))
        print("!",ans)
        flush()
        return
    # there has to be a length n+1 path in this dag i think???
    q = list()
    for snth in range(1,n*n+2):
        if nodes[snth].deg == 0:
            q.append(snth)
    while len(q) != 0:
        x = q.pop()
        nd = nodes[x].chain+1
        for e in nodes[x].edges.keys():
            if nd > nodes[e].chain:
                nodes[e].chain = nd
                nodes[e].prev = x
            nodes[e].deg -= 1
            if nodes[e].deg == 0: q.append(e)
    for snth in range(1,n*n+2):
        if nodes[snth].chain > n:
            #solution(nodes,"nodes")
            ans = [snth]
            for _ in range(nodes[snth].chain-1):
                ans.append(nodes[ans[-1]].prev)
            ans.reverse()
            ans = " ".join(map(str,ans))
            print("!",ans)
            flush()
            return
    # if not this one then DEFINITELY this one
    q = list()
    for snth in range(1,n*n+2):
        if nodes2[snth].deg == 0:
            q.append(snth)
    while len(q) != 0:
        x = q.pop()
        nd = nodes2[x].chain+1
        for e in nodes2[x].edges.keys():
            if nd > nodes2[e].chain:
                nodes2[e].chain = nd
                nodes2[e].prev = x
            nodes2[e].deg -= 1
            if nodes2[e].deg == 0: q.append(e)
    for snth in range(1,n*n+2):
        if nodes2[snth].chain > n:
            #solution(nodes2,"nodes2")
            ans = [snth]
            for _ in range(nodes2[snth].chain-1):
                ans.append(nodes2[ans[-1]].prev)
            ans = " ".join(map(str,ans))
            print("!",ans)
            flush()
            return
    
        
for _ in range(readint()):
    n = readint()
    solve(n)
