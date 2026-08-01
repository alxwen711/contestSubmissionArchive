import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
single element deletion -> 1 point
everything else depends on distance, intentionally choose the longest?
use a dp to find a maximal set?

1 2 3 4 1 5 6 6 7 5 

a maximal set will not have any pairs remaining

dp[-1] may NOT be the best option
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    prev = [-1]*(n+1)
    index = [-1]*(2*n)
    dp = [0]*(2*n) # only considering full segments
    mv = 0
    for i in range(2*n):
        # base case
        if i != 0:
            dp[i] = mv
        if prev[ar[i]] == -1:
            # add to tracker
            prev[ar[i]] = i
        else:
            # possibly remove this pair
            base = (i-prev[ar[i]]+1)**2
            possible = base+dp[prev[ar[i]]]
            if possible > dp[i]:
                dp[i] = possible
                index[i] = prev[ar[i]]
        mv = max(mv,dp[i])
    bestptr = -1
    ans = -1
    for ii in range(2*n):
        if dp[ii]+(2*n-1-ii) > ans:
            ans = dp[ii]+(2*n-1-ii)
            bestptr = ii
    br = list()
    ptr = bestptr
    while ptr != -1:
        if index[ptr] == -1:
            br.append(ar[ptr])
            ptr -= 1
        else:
            ptr = index[ptr]-1
    print(ans+len(br))
            
