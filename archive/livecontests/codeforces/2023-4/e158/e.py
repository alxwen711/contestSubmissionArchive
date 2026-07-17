import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
straight line will compress to two points
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.edges = list()

def solve():
    n = readint()
    ar = readar()
    nodes = list()
    for i in range(n):
        nodes.append(Node(ar[i]))
    for j in range(n-1):
        a,b = readints()
        nodes[a-1].edges.append(b-1)
        nodes[b-1].edges.append(a-1)
        

for _ in range(readint()):
    print(solve())
