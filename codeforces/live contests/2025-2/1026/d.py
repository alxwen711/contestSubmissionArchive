import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
graph search?
processing sequentially always works
each branch is limited to its minimum edge count?
maybe heap search is better

can you finish with at most x batteries? (binary search)
how to use at most condition rather than exact condition?

self example gives incorrect path on 9 but still makes it to the end
changing a node so the answer is 10 would not track with this method
"""

class Node:
    def __init__(self,x):
        self.base = x
        self.edges = {}

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    nodes = list()
    for i in range(n):
        nodes.append(Node(ar[i]))
    for _ in range(m):
        s,t,w = readints()
        nodes[s-1].edges[t-1] = w
    
