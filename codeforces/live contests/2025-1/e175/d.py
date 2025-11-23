import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
how many nodes were in the previous layer -1 is the number of possible outs
1
2 (1)
3 (1)
2 (2)

root -> 4, 4, 4, ...
1
4
12 (3)
36 (9)
"""

def solve():
    n = readint()
    edges = readar()
    children = list()
    for _ in range(n):
        tmp = list()
        children.append(tmp)
    for i in range(n-1):
        children[edges[i]-1].append(i+1)
    level = [-1]*n
    level[0] = 0
    q = [0]
    l = 0
    counts = [1]
    while len(q) != 0:
        c = 0
        l += 1
        nq = list()
        for p in q:
            for r in children[p]:
                nq.append(r)
                level[r] = l
                c += 1
        q = nq
        if c != 0: counts.append(c)
    m = 998244353
    indiv = [1,1]
    total = [1,counts[1]]
    for j in range(2,len(counts)):
        indiv.append((indiv[-1]*(counts[j-1]-1)) % m)
        total.append((indiv[-1]*counts[j]) % m)
    #print(indiv)
    #print(total)
    return sum(total) % m
    
for _ in range(readint()):
    print(solve())
