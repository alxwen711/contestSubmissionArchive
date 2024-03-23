import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
vertices are considered intersections
choosing any 2 is fine, 3+ is a bit trickier
"""

class Node:
    def __init__(self):
        self.edges = list()

for _ in range(readint()):
    n = readint()
    ans = n+1
    ar = list()
    for _ in range(n):
        ar.append(Node())
    for _ in range(n-1):
        a,b = readints()
        a -= 1
        b -= 1
        ar[a].edges.append(b)
        ar[b].edges.append(a)
        
