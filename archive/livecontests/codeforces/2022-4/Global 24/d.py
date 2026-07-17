import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
at least n//2 removals needed all adjacent
odd vertices can only remove n-2, even remove n-1 max
3,16,40,
2d dp somehow
"""

n,p = readints()
