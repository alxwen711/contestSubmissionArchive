import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
minimizing the number of binary search iterations for a given array
then sum this operation over ALL good arrays


"""

p = 676767677

for _ in range(readint()):
    n,m = readints()
    
