import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
num of subarrays where xor is not a square value
only up to 512 possible squares, idea is to
subtract from maximum value?
still at least 100 mill operations if O(n)
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    ans = (n*n+n)//2
    for j in range(512):
        ans -= ?
