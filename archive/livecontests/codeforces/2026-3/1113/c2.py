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

probably has different approach if wa2

if it's fully encapsulated, remove it
else this is a single value, then just add 1?

use stack

1 2 3 2 3 1
only +1 if it's a dummy value

1 2 3 4 5 1 2 3 4 6 5 7 7 8 8 6

(the 5 is counted again

(this one seems to have the issue of assuming last pair leads to max)

really tempted to use seg tree here

either assume a value is chosen individually or in the full pairing??
"""


for _ in range(readint()):
    n = readint()
    ar = readar()
    prev = [-1]*(n+1)
    #index = [-1]*(2*n)
    dp = [0]*(2*n) # only considering full segments
    mv = 0
    for i in range(2*n):
        # base case
        dp[i] = max(dp[i],mv+1) # assume whatever was previous and solo pick
        if prev[ar[i]] == -1:
            # add to tracker
            prev[ar[i]] = i
        else:
            # possibly remove this pair
            possible = (i-prev[ar[i]]+1)**2
            if prev[ar[i]] != 0:
                possible += dp[prev[ar[i]]-1]
            if possible > dp[i]:
                dp[i] = possible
                #index[i] = prev[ar[i]]
        mv = max(mv,dp[i])
    print(max(dp))
