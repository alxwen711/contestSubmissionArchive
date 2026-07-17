import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# rest in pepperoni tree problems
"""
O(n) methods for tree processing?
1 is the root node, may not be the optimal point
track depths, find the ancestor, track maximum distance
between the nodes // 2?
track ancestor depth, if direct ancestor, take difference
else, add opposing children's max distances - 2*ancestor depth?
also need a way to track ancestors without iterating 1 at a time
else tree with two long branches can break
cannot directly track all ancestors in each node, could take O(n^2)

track depth with bfs, this can also find direct parent
maybe only store some ancestor nodes depending on layer level
if sharing the same ancestor with another, then can keep dropping
levels until differing, then start building up from there to find
the ancestor
log n layer points are needed to prevent tle, but there will be a counter
setup each time that results in O(n/log n) = O(n) layer traversals

dfs may be involved, track depths with dfs list and first occurance of each
then range query on depth array for min, track to the ancestor node
then use above algo?
how to track specific index?
"""

class Node:
    def __init__(self,ID):
        self.ID = ID
        self.depth = 0
        self.connected = list()

    def add(self,x):
        self.connected.append(x)


for i in range(readint()):
    n,q = readints()
    nl = ["nun"]
    for nth in range(n):
        nl.append(Node(nth+1))
    for j in range(n-1):
        a,b = readints()
        nl[a].add(b)
        nl[b].add(a)
