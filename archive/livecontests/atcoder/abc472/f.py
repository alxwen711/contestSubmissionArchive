import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
counter clockwise point order
determine the centroid of the shape on the right (divided by line)
there is binary search ideas to find the centroid, but has to be done
practically instantly

n <= 30000, maybe some weird sqrt decomp?
"""

n,q = readints()
