import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n limit of 100000 but 4 seconds, potential O(n^1.5)
only need the kth smallest value (this can be ANYTHING)

from each value traversing left, somehow have to find the next bit
setup that changes the value? (not always cmp to first value in subarray)

3rd case: compute expected of 4, singular special value acts as dist 5
either gets grouped with one of the other values, or 4 values picked first
then the last value is special treating it as a normal
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
