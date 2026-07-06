import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
k is either 0 or 1
i + j must be odd
array colouring can be rbrbrbrbrb...
where 1 r and 1 b must be used

if k == 1: all r must be odd and b must be even
or vice versa

if k == 0: EVERYTHING has to be odd/even only
"""

#compute factorials
fact = [1]*100003
m = 1000000007
for ii in range(1,100003):
    fact[ii] = (fact[ii-1]*ii) % m

for i in range(readint()):
    n,k = readints()
    ar = readar()
    odd,even = 0,0
    for j in ar:
        if j % 2 == 0: even += 1
        else: odd += 1
    if k == 0:
        if odd == 0 or even == 0: print(fact[n])
        else: print(0)
    else:
        aset,bset = (n+1)//2,n//2
        ans = 0
        if aset == odd and bset == even: ans = (fact[odd]*fact[even]+ans) % m
        if bset == odd and aset == even: ans = (fact[odd]*fact[even]+ans) % m
        print(ans)
