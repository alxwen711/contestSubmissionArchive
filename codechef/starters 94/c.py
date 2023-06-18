import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
fixate point for the 0 and determine how many ways 4
can be chosen on each side
"""

m = 1000000007

def solve(n,s):
    ar = list()
    for snth in range(n):
        x = s[snth]
        if x == "4": ar.append(0)
        elif x == "*": ar.append(1)
        else: ar.append(2)
    s = ar
    l = [0]*n
    x = 0
    inc = 1
    for i in range(n):
        aa = s[i]
        if aa == 0: x += inc
        elif aa == 1:
            x <<= 1
            x += inc
            inc <<= 1
        x = x % m
        inc = inc % m
        l[i] = x
    r = [0]*n
    x = 0
    inc = 1
    for j in range(n):
        aa = s[-j-1]
        if aa == 0: x += inc
        elif aa == 1:
            x <<= 1
            x += inc
            inc <<= 1
        x = x % m
        inc = inc % m
        r[j] = x
    r.reverse()
    ans = 0
    for k in range(1,n-1):
        if s[k] != 0: #can be 0
            ans = (ans+l[k-1]*r[k+1]) % m
    return ans
    
for i in range(readint()):
    n = readint()
    s = input()
    print(solve(n,s))
