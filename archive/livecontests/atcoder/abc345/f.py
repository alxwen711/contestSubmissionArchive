import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
each subgraph must have even number of lamps on
extra cases with if extra flicks can be allowed or not (is every subgraph 2 nodes)
upsolve this later, currently having pain on d and e
"""
