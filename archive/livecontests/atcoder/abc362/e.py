import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
n is at most 80
every length 1/2 is arithmetic subsequence
for each length, track how many subsequences with
value x required next after each iteration?
1 rule operates differently
"""
m = 998244353
n = readint()
ar = readar()
d = {}
# dictionary keys being used is
# (current sequence length,required next value in the sequence,increment for sequence)
for i in ar:
    nd = {}
    for a in d.keys():
        nd[a] = d[a]
    for b in d.keys():
        base = d[b]
        if b[0] == 1:
            v = (2,i+i-b[1],i-b[1]) # next required value and inc
            if nd.get(v) == None: nd[v] = base
            else: nd[v] = (nd[v]+base) % m
        elif i == b[1]: # hit target
            v = (b[0]+1,i+b[2],b[2])
            if nd.get(v) == None: nd[v] = base
            else: nd[v] = (nd[v]+base) % m
    v = (1,i,0)
    if nd.get(v) == None: nd[v] = 1
    else: nd[v] = (nd[v]+1) % m
    d = nd
ans = [0]*n
for j in d.keys():
    ans[j[0]-1] = (ans[j[0]-1]+d[j]) % m
print(*ans)
