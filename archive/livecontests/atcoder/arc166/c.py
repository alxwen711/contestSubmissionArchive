import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 1 -> 4
1 2 -> 12
1 3 -> under 48
2 1 -> 12
2 2 -> under 144
2 3 -> 800

there is some sort of mathematical pattern
"""
