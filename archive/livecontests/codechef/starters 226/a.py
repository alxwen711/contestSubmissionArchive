import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]

"""
cases where distinct values can be ignored
just greedy this??
assume that the first value must be included
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    d = {}
    v = 0
    ans = 1
    for i in ar:
        if i == ar[0]: v += 1
        else:
            if d.get(i) == None: d[i] = 0
            d[i] += 1
    br = list()
    for u in d.keys():
        br.append(d[u])
    br.sort()
    br.reverse()
    if n-v > k:
        for t in br:
            v += t
            ans += 1
            if n-v <= k: break
    
    print(ans)
    
    
    
    
    
    
