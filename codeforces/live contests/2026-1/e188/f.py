import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
optimal increase strategy is greedy
compute this over all subarrays?? yeah i'm not sure about this one at all
"""

n,m = readints()
ar = readar()
br = readar()

p = 998244353
