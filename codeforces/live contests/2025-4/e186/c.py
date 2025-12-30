import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
O(n^2) is allowed, basic binary search/two pointer

1 1 1 2
2 3 3 3

compute every setup with 1, then all cyclic variations are countable
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    cr = readar()
    hit = [1]*n
    for i in range(n):
        for j in range(n):
            if ar[i] >= br[j]:
                hit[(j-i) % n] = 0
    ans = sum(hit)
    hit = [1]*n
    for i in range(n):
        for j in range(n):
            if br[i] >= cr[j]:
                hit[(j-i) % n] = 0
    
    ans *= sum(hit)
    print(ans*n)
