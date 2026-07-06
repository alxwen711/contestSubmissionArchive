import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
def ex(ar,x):
    cr = list()
    for t in range(10):
        if len(ar[t]) >= 10:
            for w in range(10):
                cr.append([ar[t][-10+w],t])
        else:
            for u in range(len(ar[t])):
                cr.append([ar[t][u],t])
    cr.sort()
    cr.reverse()
    add = True
    ans = 0
    h = [0]*10
    index = x
    for m in range(len(cr)):
        v = cr[m]
        h[v[1]] += 1
        if h.count(10) != 0: return ans
        if (10-h.count(0)) < max(h): add = False
        else: add = True
        if add: ans += (index - v[0])
        index = v[0]
    if add: ans += index
    return ans

def solve(n,s):
    ar = list()
    for i in range(10):
        ar.append(list())
    ans = 0
    for j in range(n):
        ar[int(s[j])].append(j)
        #if len(ar[int(s[j])]) == 11: ar[int(s[j])].pop(0) 
        ans += ex(ar,j+1)
    return ans
"""
def solve(n,s):
    ans = 0
    for j in range(n):
        h = [0]*10
        un = 0
        mm = 0
        for k in range(j,-1,-1):
            if h[ar[k]] == 0: un += 1
            h[ar[k]] += 1
            if h[ar[k]] > mm: mm = h[ar[k]]
            if mm == 11: break
            if un >= mm: ans += 1
    return ans
    

for i in range(readint()):
    n = readint()
    s = input()
    ar = list()
    for j in range(n):
        ar.append(int(s[j]))
    print(solve(n,ar))
