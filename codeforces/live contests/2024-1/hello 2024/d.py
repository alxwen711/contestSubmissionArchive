import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
NOT the same as a normal complete binary tree
mainly that the cascading ladder system is complete
A is parents of B and C
B is parents of D and E
D is parents of F and G ...

sum is not necessarily consistent, for 5 nodes can vary from 5 to 10

same value -> height difference of 1

go highest to lowest grouping with n-1 val, if can group to singular then yes
if can be paired with n-1 val, prune n val
multiple of same val can hit here
0 1 2 2 2 2 passes
0 2 2 1 2 fails
"""
