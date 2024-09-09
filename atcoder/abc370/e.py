import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
up to 200000
either using partition or not dp collapses if first value of partition is k
-5 3 2 -5 2 3 -5 1 4 -5 4 1 pattern can cause O(n^2) 0 sums
-3 3 -3 3 -3 3 -3 3 -3 3
either add in, or reset to 0
reset can only be used if the sum is not k
using this dp only has O(n^2) sums, not exponential

d[0] = 1
d[1] = 1
d[0] = 1, d[1] = 1
d[2] = 1, d[3] = 1
d[0] = 1, d[2] = 1, d[3] = 1
d[3] = 1, d[5] = 1, d[6] = 1

adjusted from contest submission to reflect intended O(n^2) implementation
"""
"""
n,k = readints()
ar = readar()
d = {}
m = 998244353
d[0] = 1
for ii in range(len(ar)):
    i = ar[ii]
    # run inclusion of the new step
    nd = {}
    v = 0
    for j in d.keys():
        if nd.get(j+i) == None: nd[j+i] = 0
        nd[j+i] = (nd[j+i]+d[j]) % m
        if j+i != k: v = (v+d[j]) % m
    if ii != len(ar)-1: # include division barrier
        if nd.get(0) == None: nd[0] = 0
        nd[0] = (nd[0]+v) % m
    d = nd
    
ans = 0
for e in d.keys():
    if e != k: ans = (ans+d[e]) % m
print(ans)
"""

# solution after editorial understanding

n,k = readints()
ar = readar()
m = 998244353
d = {}
d[0] = 1
possiblepartitions = 1
rs = 0 # running sum
for i in range(n):
    rs += ar[i]
    completed = (possiblepartitions - d.get(rs-k,0)) % m
    if d.get(rs) == None: d[rs] = 0
    d[rs] = (d[rs]+completed) % m
    possiblepartitions = (possiblepartitions + completed) % m
    if i == n-1: print(completed)
