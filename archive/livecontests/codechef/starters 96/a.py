import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
only a few elements in the middle may be unswappable
"""
for i in range(readint()):
    n,k = readints()
    ar = readar()
    br = list()
    for j in range(n):
        if j >= k or j < n-k: br.append(ar[j])
    br.sort()
    index = 0
    for l in range(n):
        if l >= k or l < n-k:
            ar[l] = br[index]
            index += 1
    print(*ar)
