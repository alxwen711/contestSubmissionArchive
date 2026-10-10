import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
find optimal subarray returning max value:
m = max(subarray)
AND every value in subarray with m
xor the subarray

there MUST be at least 2 elements
the AND step can be done at the end
just use XOR on everything then apply AND

then might be optimal to find maximal XOR with
as large of a subarray as possible?

from highest to lowest bit:
if 0 instances -> no change
if odd

determine if a subarray where XOR covers x and maximum value covers x

suspecting some sort of O(n log n) bit set idea is in play here

efficiently find maximums where form can be ?1?11?

pointer traversal does not appear to work here

matrix?
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
