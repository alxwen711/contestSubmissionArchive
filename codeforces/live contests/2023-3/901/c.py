import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
feels like a working backwards problem
finish node obviously has probability 1
leaf nodes have prob 0

nodes is at most 5000, edges is at most 200000

3rd case prob is 59/120
"""
