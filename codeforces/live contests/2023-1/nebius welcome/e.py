import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
determine if a cycle exists such that every node is either
in the cycle or a direct neighbour of the cycle
2**20 is about a million, take EVERY combination?

cycle nodes have minimum degree 2
"""

n,m = readints()
ar = list()
ar.append(0)
for i in range(n):
    ar.append(list())
for j in range(m):
    a,b = readints()
    ar[a].append(b)
    ar[b].append(a)
    
    
