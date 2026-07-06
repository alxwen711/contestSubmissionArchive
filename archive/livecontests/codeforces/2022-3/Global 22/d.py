import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if value b[x] =
n+1 -> x and all values to the left of x are less than or equal to k
0 -> x and all values to the left of x are greater than k
k = highest non special value (- 1?)
"""
def freq_dict(ar, pos = False) -> dict:
    d = {}
    if ar == None: return d
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None:
            if pos: d[x] = list()
            else: d[x] = 0
        if pos: d[x].append(i+1)
        else: d[x] += 1
    return d

def solve(n,ar,k):
    #list what values in ar -> br
    d = freq_dict(ar,True)
    sp = 0
    if d.get(0) == None: sp = n+1
    ans = list()
    while len(ans) != n:
        if sp != 0 and sp != n+1: ans.append(sp)
        f = d[sp]
        for t in range(len(f)):
            if d.get(f[t]) == None: ans.append(f[t])
            else: sp = f[t]
    return ans


for i in range(readint()):
    n = readint()
    ar = readar()
    #determine k value
    k = 0
    for j in range(n):
        """
        if ar[j] > (j+1) and ar[j] != n+1:
            k = max(k,ar[j]-1)
        elif ar[j] < (j+1) and ar[j] != 0:
            k = max(k,ar[j])
        """
        if ar[j] > (j+1): k += 1
    if k == 0:
        if ar[0] == n+1: k = n
    print(k)
    print(*solve(n,ar,k))
