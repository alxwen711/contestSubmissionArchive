import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
easy case can use O(n^2)
hard case must be O(n)
2 6 13 3 15 5 10 8 16 9 11 18
if sorted is 1 2 3 4 5
then something like 2 1 3 5 4 takes 2 seconds to sort
(only considering 1 range query can be made right now)
"""
for i in range(readint()):
    n = readint()
    ar = readar()
    #[len-1][indent]
    mi = list()
    ma = list()
    fl = list()
    fh = list()
    tl = list()
    th = list()
    for nth in range(n):
        tl.append(nth)
        th.append(nth)
    fl.append(tl)
    fh.append(th)
    mi.append(deepcopy(ar))
    ma.append(deepcopy(ar))
    ans = list()
    tmp = [0]*n
    ans.append(tmp)
    for j in range(n-1):
        ti = list()
        ta = list()
        tl = list()
        th = list()
        tans = list()
        l = j+1
        print(fl[-1],fh[-1])
        for k in range(l,n):
            a,b = mi[j][k-l],ma[j][k-l]
            aa,bb = min(a,ar[k]),max(b,ar[k])
            ti.append(aa)
            ta.append(bb)
            x,y = fl[j][k-l],fh[j][k-l]
            if aa < a: # new min, update
                x = k-l
                y = k
            elif bb > b: # new max, no change req
                #tans.append(ans[j][k-l])
                #dummy = 1
                if x == y: # keep setup at right endpoint
                    x += 1
                    y += 1
            else: # mid
                #either +1 due to not extending fixation point or more
                y = k
                while x != k-l:
                    if ar[x-1] > ar[k]: x -= 1
                    else: break
            tl.append(x)
            th.append(y)
            tans.append(y-x)
            
        mi.append(ti)
        ma.append(ta)
        fl.append(tl)
        fh.append(th)
        ans.append(tans)
    print(fl[-1],fh[-1])
    x = 0
    for tt in ans:
        x += sum(tt)
        print(tt)
    print(x)
        
