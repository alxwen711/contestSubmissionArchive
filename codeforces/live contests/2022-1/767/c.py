import sys
import copy

def fT(h,m):
    for x in range(m+1):
        if h[x] == 0: return x
    return m+1

for i in range(int(sys.stdin.readline())):
    l = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    m = max(ar)
    h = [0]*(m+1) #0 to maximum
    for j in range(l):
        h[ar[j]] += 1
    mex = list()
    mexLen = 0
    target = -1
    hitList = list()
    for k in range(l):
        if target == -1:
            target = fT(h,m)
            for q in range(target):
                hitList.append(q)
        val = ar[k]
        h[val] += -1
        if target == 0:
            mexLen += 1
            mex.append(0)
            #break
        else:
            try:
                hitList.remove(val)
            except:
                continue
            if len(hitList) == 0:
                mexLen += 1
                mex.append(target)
                target = -1
    if len(hitList) != 0:
        hitList.sort()
        for b in range(len(hitList)):
            if hitList[b] != b:
                mexLen += 1
                mex.append(b)
    print(mexLen)
    for w in range(mexLen):
        print(mex[w], end = " ")
    print()
