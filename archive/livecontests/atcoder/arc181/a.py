import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n x x x 1
5 3 4 2 1
5 4 3 2 1
4 5 3 1 2
3 operations at minimum is always possible

1/n positions are important
"""


for _ in range(readint()):
    n = readint()
    ar = readar() # permutation
    count = 0
    for i in range(n):
        if ar[i] == i+1: count += 1
    if count == n: print(0)
    else:
        # 1 test
        d = [0]*n
        s = 0
        flag = False
        for j in range(n):
            d[ar[j]-1] += 1
            if ar[j] <= j: s += 1
            s += d[j]
            if s == j+1 and ar[j] == j+1: flag = True
        if flag: print(1)
        else:
            a = ar.index(1)
            b = ar.index(n)
            if a == n-1 and b == 0: print(3)
            else: print(2)
