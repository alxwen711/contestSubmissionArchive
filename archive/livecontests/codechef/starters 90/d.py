import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#O(n log n)
"""
all subarrays so sorting ar is allowed
optimal setup would have 2**n-1
count number of subsequences where value x is good?
such as value 5, choose 4 values lower, then 2**remaining values
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

m = 1000000007
ncr,rcn = fermat_array(100100,100100,m)
two = list()
b = 1
for hh in range(100100):
    two.append(b)
    b = (b*2) % m
    
for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    ans = 0
    for j in range(n):
        x = ar[j]
        v = fermat_comb(j,x-1,m,ncr,rcn)*two[n-j-1]
        ans += v
    print(ans % m)
        
    
    
