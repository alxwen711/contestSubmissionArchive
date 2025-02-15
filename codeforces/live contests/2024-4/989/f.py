import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
graph system
for a node without any parents, assume chance is 100%
for a node with parents, compute chances to reach specified values????
compute probabilities of going from one condition to another condition
"""

class Node:
    def __self__(self,r,b):
        self.r = r
        self.b = b
        self.v = 0
        self.deg = 0
        self.parents = list()


def solve():
    m = 998244353
    n,m,k = readints()
    nodes = list()
    pairs = list()
    for _ in range(k):
        a,b = readints()
        pairs.append((a,b))
        nodes.append(Node(a,b))
    
for _ in range(readint()):
    solve()
