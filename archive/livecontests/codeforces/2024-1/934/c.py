import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
maximum depth of the tree is the upper limit
find the center node and colour each level?
n-n-n-n has a duo center setup
could reasonably have a wide split duo node build
also capped at 2000 nodes

go from initial center, then try duoing with each other node???
"""

class Node:
    def __init__(self):
        self.deg = 0
        self.edges = list()
        self.val = -1

for _ in  range(readint()):
    n = readint()
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for _ in range(n-1):
        a,b = readints()
        a -= 1
        b -= 1
