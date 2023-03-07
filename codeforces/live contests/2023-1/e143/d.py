import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
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

def f(a,b,c):
    d = min(a,b,c)
    e = 0
    if a == d: e += 1
    if b == d: e += 1
    if c == d: e += 1
    return e

m = 998244353

n = readint()
ar = readar()
base = fermat_calc(n//3,n//6,m)
for i in range(n//3):
    base *= f(ar[3*i],ar[3*i+1],ar[3*i+2])
    base = base % m
print(base)
