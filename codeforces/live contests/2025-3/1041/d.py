import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
place n houses on north/south sides in some order
so that the m bridges do not intersect with each other
the m bridges always connect all of the houses, thus
we can assume house 1 is on north side and multiply
final ans by 2 afterwards

if legal, answer is product of factorial of node degrees
illegal if a cycle can be formed

"""

class Node:
    def __init__(self):
        self.deg = 0
        self.dist = -1
        self.edges = {}

mod = 1000000007
fact = [1]
for i in range(1,200003):
    fact.append((fact[-1]*i) % mod)


for _ in range(readint()):
    n,m = readints()
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for _ in range(m):
        a,b = readints()
        a -= 1
        b -= 1
        nodes[a].edges[b] = 1
        nodes[b].edges[a] = 1
        nodes[a].deg += 1
        nodes[b].deg += 1
    nodes[0].dist = 0
    q = [0]
    xv = -1
    flag = False
    while len(q) != 0:
        xv += 1
        nq = list()
        for k in q:
            for u in nodes[k].edges.keys():
                if nodes[u].dist == -1:
                    nodes[u].dist = xv+1
                    nq.append(u)
                elif nodes[u].dist != xv-1:
                    flag = True
        q = nq

    # no crash detected here
    #for stnh in nodes:
    #    if stnh.dist == -1:
    #        print(crashtheprogramhere)

    if flag: print(0)
    elif n == 2: print(2)
    elif n == 3: print(4)
    else:
        ans = 2
        odd = False
        even = False
        for snth in nodes:
            xx = 0
            why = 0
            for kk in snth.edges.keys():
                if nodes[kk].deg == 1:
                    xx += 1
                else:
                    why += 1
                    if why > 2: ans = 0
                    if nodes[kk].dist % 2 == 0: even = True
                    else: odd = True
            ans = (ans*fact[xx]) % mod
        if odd and even: ans = (ans*2) % mod
        print(ans)


                    
