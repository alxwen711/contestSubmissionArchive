import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
onion find + merge sorts?
only up to the 10th required
"""

class Node:
    def __init__(self,i):
        self.size = 1
        self.parent = -1
        self.l = [i]

def getparent(nodes,x):
    ans = x
    while nodes[ans].parent != -1:
        ans = nodes[ans].parent
    return ans

def m(ar,br):
    ai = 0
    bi = 0
    la,lb = len(ar),len(br)
    cr = list()
    for _ in range(10):
        if la == ai and lb == bi: break
        elif la == ai:
            cr.append(br[bi])
            bi += 1
        elif lb == bi:
            cr.append(ar[ai])
            ai += 1
        elif br[bi] > ar[ai]:
            cr.append(br[bi])
            bi += 1
        else:
            cr.append(ar[ai])
            ai += 1
    return cr

n,q = readints()
nodes = [123456789]
for i in range(n):
    nodes.append(Node(i+1))
for _ in range(q):
    ar = readar()
    if ar[0] == 1:
        a,b = ar[1],ar[2]
        pa,pb = getparent(nodes,a),getparent(nodes,b)
        if pa != pb:
            br = m(nodes[pa].l,nodes[pb].l)
            if nodes[pa].size > nodes[pb].size or (nodes[pa].size > nodes[pb].size and pa < pb):
                nodes[pb].parent = pa
                nodes[pa].size += nodes[pb].size
                nodes[pa].l = br
            else:
                nodes[pa].parent = pb
                nodes[pb].size += nodes[pa].size
                nodes[pb].l = br
    else:
        v,k = ar[1],ar[2]
        v = getparent(nodes,v)
        if len(nodes[v].l) >= k: print(nodes[v].l[k-1])
        else: print(-1)
