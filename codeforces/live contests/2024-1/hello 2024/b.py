import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
target is to get as much of the array into a total sum of 0
score is num of elements not in 0 subarray
"""

for _ in range(readint()):
    n = readint()
    s = sys.stdin.readline()[:-1]
    a = s.count("+")
    print(n-(min(a,n-a)*2))
