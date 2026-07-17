import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
note: cannot iterate through each mail carrier
distance is edge count + 1



for why try even with O(1) nCr best method thought of
where prev partial sum is reused would still use
n ^2/2 calcs on n=10^6



Greedy first use sum dp to find all possible partitions?
Have to determine best possible partition somehow since
worst case even knowing first/last is (/) is 24 choose 12
(2.5 million, can't run through 2k string fast enough)
7,5,4,4,4 is not greedy partitionable
"""
