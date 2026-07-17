import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
min operations needed to sort
(always possible in n-1 ops)
"""
for i in range(readint()):
    n = readint()
    ar = readar()
    h = [0]*(n+1)
    for j in range(n):
        h[ar[j]] = j
    ans = 0
    for k in range(1,n):
        if h[k] > h[k+1]: ans += 1
    print(ans)
    
