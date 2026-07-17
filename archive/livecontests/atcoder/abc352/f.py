import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
might be possible to greed operations to fill in possible
array, go from highest to lowest c, then by lowest involved index

last index is to multiply
"""

class state:

    def __init__(self,n):
        self.n = n
        self.s = [-1]*n
        self.a = [1]*(n+1)

    def singular(self):
        if sum(self.a) == 2 and self.s.count(-1) == 1:
            v = self.a.index(1,2)
            self.s[self.s.index(-1)] = v
            
    def extend(self,inc,ai,bi,mul):
        av,bv = self.s[ai],self.s[bi]
        if av != -1 and bv != -1:
            if av-bv == inc*mul: return [self]
            else: return []
        elif bv != -1:
            ev = bv-inc
            if mul == 1: ev = bv+inc
            if ev < 1 or ev > self.n: return []
            if self.a[ev] == 1:
                ts = state(self.n)
                ts.s = deepcopy(self.s)
                ts.a = deepcopy(self.a)
                ts.a[ev] = 0
                ts.s[ai] = ev
                return [ts]
            return []
        elif av != -1:
            ev = av-inc
            if mul == -1: ev = av+inc
            if ev < 1 or ev > self.n: return []
            if self.a[ev] == 1:
                ts = state(self.n)
                ts.s = deepcopy(self.s)
                ts.a = deepcopy(self.a)
                ts.a[ev] = 0
                ts.s[bi] = ev
                return [ts]
            return []
        else:
            sr = list()
            for i in range(self.n-inc):
                if self.a[i+1] == 1 and self.a[i+inc+1] == 1:
                    ts = state(self.n)
                    ts.s = deepcopy(self.s)
                    ts.a = deepcopy(self.a)
                    ts.a[i+1] = 0
                    ts.a[i+inc+1] = 0
                    if mul == 1: # higher on a   
                        ts.s[ai] = i+inc+1
                        ts.s[bi] = i+1
                    else: # higher on b   
                        ts.s[ai] = i+1
                        ts.s[bi] = i+1+inc
                    sr.append(ts)
            return sr
        
n,m = readints()
stateList = [state(n)]
con = list()
for _ in range(m):
    a,b,c = readints()
    con.append([-c,min(a,b),max(a,b),1 if a < b else -1])
con.sort()

def hhh(ar):
    m = 1099511628401
    x = 0
    for i in ar:
        x *= 317
        x += i
        x = x % m
    return x
for i in range(m):
    inc = abs(con[i][0])
    a,b = con[i][1]-1,con[i][2]-1
    mul = con[i][3]
    newStateList = list()
    h = {}
    for si in range(len(stateList)):
        br = stateList[si].extend(inc,a,b,mul)
        for bi in range(len(br)):
            hh = hhh(tuple(br[bi].s))
            if h.get(hh) == None:
                newStateList.append(br[bi])
                h[hh] = 1
    stateList = newStateList

ans = [0]*n    
for si in range(len(stateList)):
    stateList[si].singular()
    #print(stateList[s].s,stateList[s].a)
    for k in range(n):
        if ans[k] == 0: ans[k] = stateList[si].s[k]
        elif stateList[si].s[k] != ans[k]: ans[k] = -1
print(*ans)

