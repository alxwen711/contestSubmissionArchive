import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
dividing by maximum will make all prices 1 (absolute maximum possible val)
prices only go up to 200000

possible to just brute force here?
computing all multiples is only about 2.4 million operations?
how to then get each total fast enough?

only consider non-1 prices, every x div will keep 1->1

full costs of 2 to 6 can be done by finding every value mod 60,
adding back in missing remainders, then dividing entire number
pair computation takes O(n) time


"""


for _ in range(readint()): # only 10 testcases
    n,y = readints()
    ar = readar()
