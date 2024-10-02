import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
you want type a and type b values in each pair
type a vals are as low as possible
type b vals are as high as possible
ideally for n, a goes from 1 to n/2
b goes from n/2+1 to n

Easy constraints:
at least 1 value in each pair does not appear
if 1 empty -> check if it should be a/b
2 empty, both need to be included, *2 for swap case

Hard constraints:
some values are "locked out", take top/bot halves for a/b
"""

def fermat_calc(n: int, k: int, r: int) -> int:
    if k > n or r == 1: return 0
    if n == 0 or k == 0: return 1
    
    #numerator*denominator**(r-2) % r
    num,dom = 1,1
    for i in range(n-k+1,n+1):
        num = (num*i) % r
    for j in range(1,k+1):
        dom = (dom*j) % r
    return num*pow(dom,r-2,r) % r


def fermat_array(n: int, k: int, r: int):
    if k >= r or r < 3: return None, None 
    arLen = max(n,k)+3 #array length
    factorials = [0]*arLen
    inverses = [0]*arLen
    factorials[0], inverses[0] = 1,1
    for i in range(1,arLen):
        factorials[i] = factorials[i-1]*i % r
        inverses[i] = pow(factorials[i],r-2,r)
    return factorials, inverses


def fermat_comb(n,k,r,facts,invs) -> int:
    if facts == None or invs == None or r == 0: return -1 #array or div 0 error
    #trivial cases
    if k > n or r == 1: return 0 
    if n == 0 or k == 0: return 1
    return facts[n]*invs[k]*invs[n-k] % r

m = 998244353

facts,invs = fermat_array(200000,200000,m)


for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 1
    a,b = n,n
    h = [1]*(2*n+1)
    h[0] = 0
    for j in range(n):
        c = ar[2*j]
        d = ar[2*j+1]
        if c != 0 and d != 0:
            a -= 1
            b -= 1
            h[c] = 0
            h[d] = 0
    br = list()
    for k in range(2*n+1):
        if h[k] == 1: br.append(k)
    x = -1
    if a != 0: x = br[a] # this value or larger -> b
    for i in range(n):
        c = ar[2*i]
        d = ar[2*i+1]
        if c == 0 and d == 0: ans = (ans*2) % m
        elif c == 0:
            if d >= x: b -= 1
            else: a -= 1
        elif d == 0:
            if c >= x: b -= 1
            else: a -= 1
        # last case is for hard
    ans = (ans*facts[a]*facts[b]) % m
    print(ans)
