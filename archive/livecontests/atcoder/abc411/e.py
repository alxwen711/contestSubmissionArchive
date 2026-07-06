import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
figure out what to do with
1 1 1 1 1 2
1 1 1 1 1 3
1 1 1 1 1 4
1 1 1 1 1 5
...

the order in which dice are rolled does not matter
"""

n = readint()
v = {}
for j in range(n):
    ar = readar() # length 6
    for i in range(6):
        if v.get(ar[i]) == None: v[ar[i]] = list()
        v[ar[i]].append(j)
vals = list(v.keys())
vals.sort()
vals.reverse()

base = [0,0,0,0,0,0,n]
base2 = [6]*n
prob = 1
m = 998244353
denom = pow(6,n,m)
denom = pow(denom,m-2,m)
ans = 0
for a in vals:
    # decrease counts
    for c in v[a]:
        base[base2[c]] -= 1
        base2[c] -= 1
        base[base2[c]] += 1
    # compute inv odds
    numer = 1
    for snth in range(7):
        numer = (numer*pow(snth,base[snth],m)) % m
    invodd = (numer*denom) % m
    ans = (ans+a*(prob-invodd)) % m
    prob = invodd
print(ans)
    

        
