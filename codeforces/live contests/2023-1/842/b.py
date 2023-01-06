import sys
from copy import deepcopy
from math import ceil
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = readar()
    br = deepcopy(ar)
    br.sort()
    index = 0
    for j in range(n):
        if br[index] == ar[j]: index += 1
    remain = n-index
    print(ceil(remain/k))
