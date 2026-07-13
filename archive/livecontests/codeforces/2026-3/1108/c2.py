import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
after the -1 section, there are two scenarios:

0 case -> start on positive, each positive sum must be grouped
-1 case -> start on negative, will drop to some -a-1 then needs direct counter

at each point, can then decide if you want to attempt counteracting or not
if counteracting, then the next set of values MUST be used to solve (must be +1)
otherwise, run even count again
"""
mod = 1000000007

for _ in range(readint()):
    n = readint()
    ar = readar()
    x = 0
    for i in range(n):
        if ar[i] == -1: x += 1
        else: break
    
    br = list()
    cr = list()
    if x != n:
        chain = 0
        prev = ar[x]
        for j in range(x,n):
            if prev == ar[j]: chain += 1
            else:
                br.append(chain)
                cr.append(prev)
                chain = 1
                prev = ar[j]
        br.append(chain)
        cr.append(prev)
    casea = 1
    caseb = 0
    if x != 0:
        casea = pow(2,x-1,mod)
        caseb = casea

    # solve casea
    for b in br:
        casea = (casea*pow(2,b-1,mod)) % mod
    #print(casea)
    # solve caseb
    if caseb != 0:
        dp = [caseb,0,0] # [not pushed, attempt, complete]
        target = 0
        for l in range(len(br)):
            pushval = pow(2,br[l]-1,mod)
            # determine completed recycle cases
            dp[2] = (dp[2]*pushval) % mod
            if cr[l] == target: # fix solved cases
                dp[2] = (dp[1]*pushval+dp[2]) % mod
            # determine the not pushed
            dp[0] = (dp[0]*pushval) % mod # even outs
            dp[1] = dp[0] # odd outs (and removing failed attempts)
            target = cr[l] + 1
            #print(dp)
            
        casea = (casea+dp[2]) % mod
    print(casea)
    
    




