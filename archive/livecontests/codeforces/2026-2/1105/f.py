import sys
from itertools import product,combinations

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# brute force small cases and pray some pattern emerges

"""
(1)
2 1
12 18 8
72 216 228 81
480 2400 4400 3500 1024
3600 27000 75000 99000 63030 15625
30240 317520 1234800

left side is n!*(n-1)
right side is (n-1)**n

4*3*2*1*3 (4,18 -> 2*3*3)
4*3*2*3*3 (6,36 -> 2*2*3*3)
4*3*(2*3*3+1) (4,57 -> 3*19)
3*3*3*3 (1,81 -> 3**4)

543214
543254

6543215
6543535
m = 2 -> nth triangular numbers (1**2, 3**2, 6**2, 10**2)*(n-1)!
"""

class Node:
    def __init__(self,x):
        self.edges = x
        self.hit = 0

n = 7
m = 3
p = 998244353
ans = 0
ar = [i for i in range(n)]
sv = list(combinations(ar,m))
for p in product(ar,repeat = n):
    # check the permutation if legit
    flag = True
    for j in range(n):
        if p[j] == j:
            flag = False
            break
    if flag:
        # construct the graph
        nodes = list()
        for k in range(n):
            nodes.append(Node(p[k]))
        # determine validity
        for c in sv:
            q = list()
            hc = 0
            for u in c:
                nodes[u].hit = 1
                q.append(u)
                hc += 1
            # fill in search
            while len(q) != 0:
                y = q.pop()
                if nodes[nodes[y].edges].hit == 0:
                    q.append(nodes[y].edges)
                    hc += 1
                    nodes[nodes[y].edges].hit = 1
            if hc == n:
                #print(p,c)
                ans += 1
            # reset graph
            for w in range(n):
                nodes[w].hit = 0
        #print(ans,p)
print(ans)







                
