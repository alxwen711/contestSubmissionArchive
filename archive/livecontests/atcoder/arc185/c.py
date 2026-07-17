import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
# solution needs to be n log n
# x is at most 1000000, all values are at most x

dp? [number of values taken][value] = last index, like this is n^2

1 2 3 4
distance 1 groups -> 4 times
distance 2 groups -> 2 times
distance 3 groups -> 1 time

this can be used to compute the answer in n^2 time, needs n log n (or 100n)
"""
n,x = readints()
ar = readar()
indexes = {} # backwards reference
for i in range(n):
    indexes[ar[i]] = i+1
ar.sort()
