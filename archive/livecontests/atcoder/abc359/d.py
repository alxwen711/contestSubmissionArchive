import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
n is at most 1000
k is at most 10

only required to track last k chars in the string
"""

def isPal(i,n):
    ar = list()
    for _ in range(n):
        ar.append(i % 2)
        i //= 2
    #ar.reverse()
    for ii in range(n//2):
        if ar[ii] != ar[-ii-1]: return False
    return True

n,k = readints()
s = sys.stdin.readline()[:-1]

no = list()
yes = list()
for i in range(2**k):
    if isPal(i,k): no.append(i)
    else: yes.append(i)
mod = 998244353
dp = [0]*(2**k)
limit = 2**k
dp[0] = 1
for j in range(n):
    ndp = [0]*(2**k)
    for a in yes:
        index = a*2
        if index >= limit: index -= limit
        if s[j] != "B": ndp[index] = (ndp[index]+dp[a]) % mod
        if s[j] != "A": ndp[index+1] = (ndp[index+1]+dp[a]) % mod
    if j < k:
        for a in no:
            index = a*2
            if index >= limit: index -= limit
            if s[j] != "B": ndp[index] = (ndp[index]+dp[a]) % mod
            if s[j] != "A": ndp[index+1] = (ndp[index+1]+dp[a]) % mod
    
    dp = ndp
ans = 0
for snth in yes:
    ans += dp[snth]
print(ans % mod)
