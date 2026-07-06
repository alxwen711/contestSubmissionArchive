import sys
from math import gcd
#from random import randint

#chance of false positive is about 1/4^trials?
#can't use sieve as 10^14 feels too big


def prime(n: int) -> bool:
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n <= 1: return False
    for snth in [3,5,7,11,13,17,19]:
        if n == snth: return True
        if n % snth == 0: return False
    d,s = n-1,0
    while d % 2 == 0:
        s += 1
        d = d // 2
    for a in range(2,min(n-1,20)):
        #a = randint(2,n-2)
        if trial(n,s,a,d): return False
    return True


def trial(n: int, s: int, a: int, d: int) -> bool:
    val = pow(a,d,n)
    if val == 1 or val == n-1: return False
    for i in range(s-1):
        val = pow(val,2,n)
        if val == n-1: return False
    return True

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
br = readar()
ans = 0
x = ar[0]
y = br[0]
ar.append(x)
br.append(y)
#print(x,y)
#if prime(x+y): ans += 1
d = {}
for i in range(n):
    px,py = ar[i+1],br[i+1]
    dx,dy = px-x,py-y
    if dx == 0:
        m = 1
        if dy < 0: m = -1
        for j in range(abs(dy)):
            y += m
            #print(x,y)
            if x+y in d: ans += 1
            elif prime(x+y):
                ans += 1
                d[x+y] = 1
    elif dy == 0:
        m = 1
        if dx < 0: m = -1
        for joue in range(abs(dx)):
            x += m
            #print(x,y)
            if x+y in d: ans += 1
            elif prime(x+y):
                ans += 1
                d[x+y] = 1
    else:
        f = gcd(abs(dx),abs(dy))
        mx = dx//f
        my = dy//f
        for k in range(f):
            x += mx
            y += my
            #print(x,y)
            if x+y in d: ans += 1
            elif prime(x+y):
                ans += 1
                d[x+y] = 1
print(ans)
    
