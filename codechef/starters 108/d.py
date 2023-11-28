import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
If sum of array is negative, impossible, otherwise possible
-2 1 3 1 1 -4 takes 5 moves?
"""

def solve(n,ar):
    br = list()
    for i in range(n-1):
        br.append((abs(ar[i]-ar[i+1]),i))
    br.sort()
    br.reverse()
    d = {}
    s = set()
    seg = [0]*(n-1)
    ans = n
    for limit in range(2,n+1):
        while len(br) != 0:
            if br[-1][0] <= limit:
                x = br[-1][1]
                br.pop()
                #fill in x segment
                l,r = 0,0
                if x != 0: l = seg[x-1]
                if x != n-2: r = seg[x+1]
                if l == 0 and r == 0: # 1 seg
                    seg[x] = 1
                    if d.get(1) == None: d[1] = 0
                    d[1] += 1
                    if d[1] == 1 and limit == 2: s.add(1)
                elif l == 0: #right side seg
                    seg[x] = r+1
                    seg[x+r] += 1
                    d[r] -= 1
                    if d[r] == 0 or (r+5) < limit: s.discard(r)
                    if d.get(r+1) == None: d[r+1] = 0
                    d[r+1] += 1
                    if d[r+1] == 1 and (r+5) >= limit: s.add(r+1)
                elif r == 0: #left side seg
                    seg[x] = l+1
                    seg[x-l] += 1
                    d[l] -= 1
                    if d[l] == 0 or (l+5) < limit: s.discard(l)
                    if d.get(l+1) == None: d[l+1] = 0
                    d[l+1] += 1
                    if d[l+1] == 1 and (l+5) >= limit: s.add(l+1)
                else: #full extend
                    nl = l+r+1
                    seg[x-l] = nl
                    seg[x+r] = nl
                    d[l] -= 1
                    if d[l] == 0 or (l+5) < limit: s.discard(l)
                    d[r] -= 1
                    if d[r] == 0 or (r+5) < limit: s.discard(r)
                    if d.get(nl) == None: d[nl] = 0
                    d[nl] += 1
                    if d[nl] == 1 and (nl+5) >= limit: s.add(nl)
            else: break
        dlist = list()
        for u in s:
            if (u+5) < limit: dlist.append(u)
            else: ans += max(0,d[u]*(u+2-limit))
        for v in dlist:
            s.discard(v)
        #print(limit,ans)
    return ans
for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
