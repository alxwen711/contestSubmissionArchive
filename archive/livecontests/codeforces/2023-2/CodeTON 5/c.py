import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
dp idea with knowing best removal of prefix
"""
def solve(n,ar):
    first = [-1]*(n+5)
    best = [999999999]*(n+5)
    first[ar[0]] = 0
    dp = [0]*n
    
    dp[0] = 1
    for i in range(1,n):
        c = dp[i-1]+1
        #dp[i] = dp[i-1]+1
        x = ar[i]
        if first[x] == -1:
            first[x] = i
            dp[i] = c
            best[x] = c
        elif first[x] == 0:
            dp[i] = 0
            best[x] = 0 
        else:
            #if dp[first[x]-1] < best[i]:
            #    dp[i] = dp[first[x]-1]
            best[x] = min(dp[first[x]-1],best[x])
            dp[i] = min(c,best[x])
            first[x] = i
    #print(dp)
    #print(first)
    #print(best)
    return n-dp[-1]

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
