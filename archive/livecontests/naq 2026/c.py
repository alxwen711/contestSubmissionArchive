import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
initially force longer -> shorter
order by maximal dimension
if in direct conflict, impossible
else find # of placements
possible to 90 deg rotate if l != w
also frequency count
"""

def f(x,y):
    a = x[0]-y[0]+1
    b = x[1]-y[1]+1
    if min(a,b) <= 0: return 0
    v = a*b
    if y[0] == y[1]: return v
    # check if rotatable
    c = x[0]-y[1]+1
    d = x[1]-y[0]+1
    if min(c,d) > 0: v += c*d
    return v

m = 998244353

facts = [1,1]
for i in range(2,100002):
    facts.append((facts[-1]*i) % m)

for _ in range(readint()):
    n = readint()
    d = {}
    ordering = list()
    for _ in range(n):
        a,b = readints()
        if a < b: a,b = b,a
        if d.get((a,b)) == None:
            d[(a,b)] = 0
            ordering.append((a,b))
        d[(a,b)] += 1
    ordering.sort()
    ordering.reverse()
    ans = 1
    # do factorials first
    for i in range(len(ordering)):
        ans = (ans*facts[d[ordering[i]]]) % m
    
    # check if possible
    for j in range(len(ordering)-1):
        v = f(ordering[j],ordering[j+1])
        ans = (ans*v) % m
        if ans == 0: break
    if ordering[0][0] != ordering[0][1]:
        ans = (ans*2) % m
    print(ans)
