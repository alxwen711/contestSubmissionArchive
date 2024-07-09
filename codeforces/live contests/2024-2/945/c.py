import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
permutation problem, assign highest with lowest and vice versa
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    one = ar.index(1)
    inc = 1
    if one % 2 == 1: inc += 1
    br = list()
    for i in range(n//2-1):
        br.append(ar[inc+2*i])
    #print(br) # debug
    br.sort()
    d = [0]*(n+1)
    for j in range(n//2-1):
        d[br[j]] = n-j
    v = n-(n//2-1)
    for k in range(1,n+1):
        if d[k] == 0:
            d[k] = v
            v -= 1
    #print(d) # debug
    ans = list()
    for c in ar:
        ans.append(d[c])
    print(*ans)
