import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 1 -> 2
2 1 -> 3
3 2 -> 7
1 -> 1,2
2 -> 1,3,4
3 -> 1,4,7,8
4 -> 1,5,11,15,16


n k = row n+1 of pascal's triangle, sum of first k+1 elements

4 choose 0,1,2,3, take sum
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

a,b = readints()
m = 1000000007
if a <= b: print(pow(2,a,m))
elif b == 0: print(1)
else:
    ar,br = fermat_array(a,b,m)
    ans = 0
    for i in range(b+1):
        ans = ans + fermat_comb(a,i,m,ar,br)
    ans = ans % m
    print(ans)
        
