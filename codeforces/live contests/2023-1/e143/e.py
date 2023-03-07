import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
idea is to make a hill structure
if something starts off too high it can be decreased by 1 MP until hill attainment
1 2 3 4 5 4 3 2 1
O(n) is doable
choose by potential? (max mp saving potential)
each peak will have varying hill shapes
midpeak not always best, proof with 7,8,8,2,1
some sort of dp idea? can't see how scuffed greedy works here
"""

for i in range(readint()):
    n = readint()
    ar = readar()
