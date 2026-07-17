import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
some sort of arbritary chain system,
in some (not all cases), can choose
one particular to be last and then
build a full scared chain from there
seeing a directed tree structure(s)
cases like 2 1 4 3 have multiple trees
then find the lowest cost start point
(determine the cycle by traversing up parents?)

find parent cycle from unaccounted nodes
choose lowest parent
dfs system (note each node only has 1 parent)
once done, reverse list for answer
"""

class Node:
    def __init__(self,ID):
        self.ID = ID
        self.parent = -1
        self.children = list()
        

for i in range(readint()):
    n = readint()
    ar = readar()
    cr = readar()
    ans = list()
    #create graph(s)
    nodes = [0]
    for snth in range(1,n+1):
        nodes.append(Node(snth))
    for j in range(n):
        nodes[j+1].parent = ar[j]
        nodes[ar[j]].children.append(j+1)
    hit = [0]*(n+1)
    for k in range(1,n+1):
        if hit[k] == 0: #not searched yet
            # get cycle
            d = {}
            l = list()
            pt = k
            while True:
                if d.get(pt) != None: break
                else: d[pt] = 1
                l.append(pt)
                pt = nodes[pt].parent
            head = -1
            hc = 9999999999999999999
            #br = list()
            for a in range(len(l)): #cycle through candidate heads
                ch = l[-a-1]
                #br.append(ch)
                if cr[ch-1] < hc:
                    head = ch
                    hc = cr[ch-1]
                if l[-a-1] == pt: break #end of cycle
            #print("candidate heads:",br)
            q = list()
            q.append(head)
            hit[head] = 1
            #dfs
            while len(q) != 0:
                x = q.pop()
                ans.append(x)
                for b in nodes[x].children:
                    if hit[b] == 0:
                        hit[b] = 1
                        q.append(b)
    ans.reverse()
    print(*ans)
