import sys

from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
likely O(n^2) from constraint

1 1 1 1 2 2 2
1 2 1 2 1 2 1

1 1 3 3 5 5 5
1 5 5 3 1 3 5

the full median of the array must be the median chosen?

can then determine every valid subarray that works

some weird parent to child traversal to determine longest possible path
"""

class Node:
    def __init__(self):
        self.children = list()
        self.score = 0

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = deepcopy(ar)
    br.sort()
    x = br[n//2]
    nodes = list()
    for _ in range(n+1):
        nodes.append(Node())

    # get all subarrays with median x
    #sar = list()
    for i in range(n):
        high = 0
        low = 0
        exact = 0
        for j in range(i,n):
            if ar[j] == x: exact += 1
            elif ar[j] > x: high += 1
            else: low += 1
            if (j-i) % 2 == 0:
                diff = abs(high-low)
                if exact >= diff:
                    nodes[i].children.append(j+1)
                    #sar.append((i,j))
                    
    # compute longest path in the DAG that starts from 0
    hittable = [0]*(n+1)
    hittable[0] = 1
    for j in range(n):
        if hittable[j]:
            sc = nodes[j].score + 1
            for k in nodes[j].children:
                nodes[k].score = max(nodes[k].score,sc)
                hittable[k] = 1
    print(nodes[n].score)
    #print(sar)
