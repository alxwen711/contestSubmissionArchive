import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
possible to calculate one sum, then need to add/sub
subtrees in some sort of way
select head of tree, subtree calc is based on running sum
and total cost (running sum is total added cost, not actual)
then some sort of way of adding/subbing branches?
"""
