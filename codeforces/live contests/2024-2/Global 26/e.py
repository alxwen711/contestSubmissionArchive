import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

class Node:
    def __init__(self):
        self.edges = list()

def solve(n):
    nodes = [456]
    for _ in range(n):
        nodes.append(Node())
    for _ in range(n-1):
        a,b = readints()
        nodes[a].edges.append(b)
        nodes[b].edges.append(a)
        

for _ in range(readint()):
    print(solve(readint()))
