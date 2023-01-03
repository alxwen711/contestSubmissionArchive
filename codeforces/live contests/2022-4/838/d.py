import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

class Node:
    def __init__(self,ID):
        self.ID = ID
        self.next = 1
        self.prev = 0
        self.r = -1
        self.l = -1


def solve(n):
    if n == 2:
        print("! 1 2")
        flush()
        return
    ar = list()
    for i in range(n):
        ar.append(Node(i))
    for j in range(n):
        ar[j].next = ar[(j+1) % n]
        ar[j].prev = ar[(j-1) % n]
        print("?",j+1,(j+1)%n+1)
        flush()
        x = readint()
        ar[j].l = x
        ar[(j+1) % n].r = x
        
    firstcycle = list()
    for k in range(n):
        if ar[k].l != ar[k].r: firstcycle.append(k)
    
    nodeCount = len(firstcycle)
    ll = list()
    for m in range(nodeCount):
        ar[firstcycle[m]].next = ar[(firstcycle[(m+1) % nodeCount])]
        ar[firstcycle[m]].prev = ar[(firstcycle[(m-1) % nodeCount])]
        if ar[firstcycle[m]].next.ID != (firstcycle[m]+1) % n:
            ar[firstcycle[m]].l = -1
            ar[firstcycle[m]].next.r = -1
            ll.append([ar[firstcycle[m]].ID,ar[firstcycle[m]].next.ID])
    breaker = 0
    guesses = n
    while nodeCount > 2:
        breaker += 1
        for s in range(len(ll)):
            if guesses == 0:
                print("!",ar[firstcycle[0]].ID+1,ar[firstcycle[0]].next.ID+1)
                flush()
                return
            print("?",ll[s][0]+1,ll[s][1]+1)
            flush()
            x = readint()
            ar[ll[s][0]].l = x
            ar[ll[s][1]].r = x
            guesses -= 1
            

        nextcycle = list()
        #determine new cycle
        for u in range(len(firstcycle)):
            if max(ar[firstcycle[u]].l,ar[firstcycle[u]].r)*2 >= n: #auto clear
                print("!",ar[firstcycle[u]].ID+1,ar[firstcycle[u]].next.ID+1)
                flush()
                return
            elif min(ar[firstcycle[u]].l,ar[firstcycle[u]].r) > breaker and ar[firstcycle[u]].l != ar[firstcycle[u]].r:
                nextcycle.append(firstcycle[u])

        #construct next cycle and new connections
        nodeCount = len(nextcycle)
        if nodeCount == 1:
            print("!",ar[nextcycle[0]].ID+1,ar[nextcycle[0]].next.ID+1)
            flush()
            return
        elif nodeCount == 2:
            print("!",ar[nextcycle[0]].ID+1,ar[nextcycle[1]].ID+1)
            flush()
            return
        ll = list()
        for v in range(nodeCount):
            if nextcycle[(v+1)%nodeCount] != ar[nextcycle[v]].next.ID:
                ar[nextcycle[v]].l = -1
                ar[nextcycle[(v+1)%nodeCount]].r = -1
                ll.append(nextcycle[v],nextcycle[(v+1)%nodeCount])
            ar[nextcycle[v]].next = ar[nextcycle[(v+1)%nodeCount]]
            ar[nextcycle[(v+1)%nodeCount]].prev = ar[nextcycle[v]]
            
        firstcycle = nextcycle
        
    print("!",ar[firstcycle[0]].ID+1,ar[firstcycle[0]].next.ID+1)
    flush()
    return


for i in range(readint()):
    n = readint()
    solve(n)
    r = readint()
    if r == -1: break #WA
