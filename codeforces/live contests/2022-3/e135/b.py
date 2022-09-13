import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from random import shuffle

def foo(ar):
    ans = 0
    for k in range(len(ar)):
        if ar[k] > ans: ans += ar[k]
        else: ans = 0
    return ans

for i in range(readint()):
    n = readint()
    ar = list()
    for j in range(n-2):
        ar.append(j+1)

    while foo(ar) != 0:
        shuffle(ar)
    ar.append(n-1)
    ar.append(n)
    print(*ar)
    
    
