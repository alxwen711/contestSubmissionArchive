import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
will have at least 1 lamp on every time
if any single chain from 5+ exists, can be flipped
EVERY flip case could be considered here (log n growth)

maybe there is something with topological sort?
"""
