import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
A = [1,2,4,8,16...]
no non-empty subarray sum is 0
"""
for i in range(readint()):
    n = readint()
    ar = readar()
    p,q = 0,0 #pos,neg
    for j in range(n):
        if ar[j] == 1: p += (j+1)
        else: q += (j+1)
    print(abs(p-q))
