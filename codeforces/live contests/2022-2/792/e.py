"""
if k >= n-# of 0, ans is 0
use dict to track frequency of each number
either make all numbers the same value (1)
or maximize mex score with min diff inc
"""

import sys
for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    h = [0]*n #mex tracker
    d = {}
    e = {}
    for j in range(n):
        x = ar[j]
        if x < n: h[x] = 1
        if d.get(x) == None:
            d[x] = 0
            e[x] = list()
        d[x] += 1
        e[x].append(j)
    br = list()
    cr = list()
    dk = list(d.keys())
    for m in range(len(dk)):
        br.append([dk[m],d[dk[m]]])
        cr.append([d[dk[m]],dk[m]])
    cr = sorted(cr, key = lambda x: (x[0],-x[1]))
    print(br)
    print(cr)
    if k >= n - d[0]: print(0)
    else:
        mex = 0
        for w in range(n):
            if h[w] == 0:
                mex = w
                break
        
