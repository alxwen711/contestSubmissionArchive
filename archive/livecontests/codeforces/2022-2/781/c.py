"""
find num of nodes on each level
"""
def bs(a,t):
    low = 0
    high = len(a)-1
    while high-low > 1:
        mid = (low+high)//2
        if a[mid] > t: high = mid
        else: low = mid
    return low

def sss(a,t):
    st = bs(a,t)
    x = t
    y = len(a)
    while st < y:
        if a[st] > t: x += (t-a[st])
        if x < 0: return False
        st += 1
    return True

def why(a):
    high = max(a)
    low = 0
    while high-low > 1:
        mid = (low+high)//2
        if sss(a,mid): high = mid
        else: low = mid
    return high
    

import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    d = {}
    for j in range(len(ar)):
        if d.get(ar[j]) == None:
            d[ar[j]] = list()
        d[ar[j]].append(j+2)
    layers = list()
    layers.append(1)
    queue = list()
    queue.append(1)
    ans = 1
    while True:
        l = 0
        for k in range(len(queue)):
            x = queue.pop(0)
            if d.get(x) != None:
                ans += 1
                l = 1
                m = d[x]
                layers.append(len(m))
                for p in range(len(m)):
                    queue.append(m[p])
        if l == 0: break
    #print(layers)
    layers.sort()
    h = list()
    for z in range(len(layers)):
        if layers[z] > (z+1): h.append(layers[z]-z-1)
    if len(h) != 0: ans += why(h)
    print(ans)
        
