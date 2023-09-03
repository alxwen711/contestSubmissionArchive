import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 2 -> 0
2 2 -> 2
3 2 -> 6
4 2 -> 18
5 2 -> 48
3 3 -> 27
10 3 -> 71712



x k -> 0 when x is below k
k k -> k! (permutation count)
k+1 k -> 2*k*k! (those that have a permutation) - k! (double perm overcount)
scoring zone method can lead to overcount

count how many would have 1, then 2, then 3, and so on?

maybe partial permutaions need to be tracked??
"""


n,k = readints()

for i in range(32):
    print(bin(i))
