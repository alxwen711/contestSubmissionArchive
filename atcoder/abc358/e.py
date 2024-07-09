import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
at most 26 thousand lengths,
compute number of ways to insert the new chrs in string len x
choosing with repetition?
"""
def fermat_array(n: int, k: int, r: int) -> list[list[int],list[int]]:
    if k >= r or r < 3: return None, None 
    arLen = max(n,k)+3 #array length
    factorials = [0]*arLen
    inverses = [0]*arLen
    factorials[0], inverses[0] = 1,1
    for i in range(1,arLen):
        factorials[i] = factorials[i-1]*i % r
        inverses[i] = pow(factorials[i],r-2,r)
    return factorials, inverses


def fermat_comb(n: int, k: int, r: int, facts: list[int], invs: list[int]) -> int:
    if facts == None or invs == None or r == 0: return -1 #array or div 0 error
    #trivial cases
    if k > n or r == 1: return 0 
    if n == 0 or k == 0: return 1
    return facts[n]*invs[k]*invs[n-k] % r

facts,invs = fermat_array(1000,1000,998244353)

k = readint()
ar = readar()
dp = [1]
for i in range(26):
    if ar[i] != 0:
        ndp = [0]*(min(len(dp)+ar[i],k+1))
        for j in range(len(dp)):
            ndp[j] = dp[j]
        for a in range(1,ar[i]+1):
            for b in range(len(dp)):
                if (a+b) > k: break
                ndp[b+a] = (ndp[b+a]+fermat_comb(b+a,a,998244353,facts,invs)*dp[b]) % 998244353
        dp = ndp
dp[0] = 0
print(sum(dp) % 998244353)
