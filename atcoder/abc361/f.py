import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
10**18 -> max exponent is 59

any n**4,6,8,10... can be expressed as a n**2

compute exponents 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59

17 exponents, can perform bitset union here
(faster because any product > 59 = fail)
"""

def bsearch(n,m):
    low = 1
    high = 1000000000
    while high-low > 1:
        mid = (low+high)//2
        if mid**m <= n: low = mid
        else: high = mid
    if high**m <= n: return high
    return low

n = readint()
ar = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
ans = 0
for i in range(1,2**len(ar)):
    x = i
    m = 1
    mul = -1
    for j in ar:
        if x % 2 == 1:
            m *= j
            mul *= -1
        x //= 2
    if m < 60:
        ans += bsearch(n,m)*mul
print(ans-1)
