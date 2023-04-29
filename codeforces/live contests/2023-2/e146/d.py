import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
ai*bi list total values must differ by at most k
change as few bi values as possible
n is at most 3000, O(n^2) may be needed
"""

for i in range(readint()):
    n,k = readints()
    ar = list()
    br = list()
