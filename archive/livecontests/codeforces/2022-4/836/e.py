import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
cases where two rows already have time diff are impossible, ie.
1 2 x x x 
1 1 x x x 
same argument for columns
how to assign free clocks? (some positions may be determinable by setup)

h = 3
1 x 2
x 0 x
x 1 0

1 0 2
1 0 2
2 1 0
"""
