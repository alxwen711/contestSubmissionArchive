import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

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

def inverse(x,m):
    return pow(x,m-2,m)

m = 998244353
fa,iv = fermat_array(300001,300001,998244353)
ans = fermat_comb(1000,500,m,fa,iv)-fermat_comb(1000,501,m,fa,iv)
ans *= inverse(fermat_comb(802,402,m,fa,iv),m)
ans *= inverse(fermat_comb(602,302,m,fa,iv),m)
ans *= inverse(fermat_comb(402,202,m,fa,iv),m)
print(ans % m)
