import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
track maximum and minimum possible states,
upon reading a post the value would be current negative with minimum found
"""

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar()
    h = [0]*n
    for b in br:
        h[b-1] = 1
    mindp = [9999999999999999999999999]*(n+1)
    maxdp = [-999999999999999999999999]*(n+1)
    mindp[0] = 0
    maxdp[0] = 0
    for i in range(n):
        v = ar[i]
        # do not watch case
        mindp[i+1] = mindp[i]+v
        maxdp[i+1] = maxdp[i]+v
        # watch case
        if h[i]:
            mindp[i+1] = min(mindp[i+1],-maxdp[i]-v)
            maxdp[i+1] = max(maxdp[i+1],-mindp[i]-v)
    print(maxdp[n])
        
