import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
a main query consists of finding minimum positive value x
such that x to x+k-1 are not in the set
you can assume the insert/remove will not force multiset

set values go up to 2000000, k can go up to 2000000

n and m are at most 200000

when inserting a value, it should be possible to track the 
lengths of each segment

then there is some sort of binary search idea here (seg tree)

you can use ordered set to track the lengths of sets that exist
and the indices at which they start; also just inserting/removing
with automatic sort is very useful

ordered_set ftw

dictionaries are a thing (upsolving this later because i have a headache)
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    m = readint()
    for _ in range(m):
        o,v = readins()
        v = int(v)
