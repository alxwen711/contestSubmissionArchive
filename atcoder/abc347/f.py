import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
constraints are relatively low, various tricks exist
for square sums (prefix arrays)
1000x1000 grid with 250x250 squares
751x751 possible squares (500k+), needs further optimization
could create 2d sparse table with all the highest results in a region
would require too many squares to guarntee a triple exists without collision
even 2 squares has O(n^4) possiblities

areas to get for 3rd square possibility
above higher square
below lower square
left of left square
right of right square
if sharing x/y, single rectangle case
otherwise, 2 corner rects + extended boundary (4 scenarios)
current best run time is O(n^4) with above method, O(n^2 log n) is needed
"""

n,m = readints()
grid = list()
for _ in range(n):
    tmp = readar()
    grid.append(tmp)
