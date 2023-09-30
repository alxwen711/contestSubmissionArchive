import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
p,q,rm,rh
if m win, rm += 1
if h win, rh += 1
prob m win = rm/(rm+rh)
prob h win = rh/(rh+rm)

there is practically no limit on constraints,
possibly a math cheese solution

grid system can solve a case in O(n**2)
"""
#compute factorials
fact = [1]*100003
mod = 1000000007
for ii in range(1,100003):
    fact[ii] = (fact[ii-1]*ii) % mod

for i in range(readint()):
    p,q,m,h = readints()
    num = fact[m+p-1]*pow(fact[m-1],mod-2,mod)
    dom = fact[m+h+p-1]*pow(fact[m+h-1],mod-2,mod)
    dom += q
    ans = (num*pow(dom,mod-2,mod)) % mod
    print(ans)
