import sys
from queue import Queue
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

class Node:
    def __init__(self,depth,val):
        self.depth = depth
        self.val = val
        self.parent = list()
        self.children = 0


def solve(n,ar):
    h = list()
    o = list()
    for i in range(n):
        h.append(ar[i].count('1'))
        if h[i] == 0:
            o.append(Node(0,i))
    nodeList = [0]*n
    child = [0]*n
    while len(o) != 0:
        x = o.pop()
        for j in range(n):
            if ar[j][x.val] == '1' and h[j] >= x.depth+1: #child
                if nodeList[j] == 0:
                    nn = Node(x.depth+1,j)
                    nn.parent.append(x)
                    x.children += 1
                    o.append(nn)
                    nodeList[j] = nn
                else:
                    nodeList[j].parent.append(x)
                    x.children += 1
        nodeList[x.val] = x
        child[x.val] = x.children
    #print(children)
    q = Queue()
    for k in range(n):
        if child[k] == 0: q.put(k)
    ans = list()
    for oeu in range(n):
        ans.append({})
    for s in range(1,n+1):
        x = q.get()
        x = nodeList[x]
        for tt in range(len(x.parent)):
            if child[x.parent[tt].val] == 1:
                q.put(x.parent[tt].val)
            child[x.parent[tt].val] -= 1
        alist = list()
        alist.append(x)
        while len(alist) != 0:
            b = alist.pop()
            ans[b.val][s] = 1
            for ttt in range(len(b.parent)):
                alist.append(b.parent[ttt])
    
    for u in range(n):
        hhh = list(ans[u].keys())
        print(len(hhh),end=" ")
        print(*hhh)
                        

for i in range(readint()):
    n = readint()
    ar = list()
    for j in range(n):
        t = input()
        ar.append(t)
    solve(n,ar)

