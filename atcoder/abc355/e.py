import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
take larger left queries until passes right
before this then greedily set queries to hit
right target
there are subtraction outs

extend ranges to various exponents of 2, determine the min

this is a graph problem isn't it.
you create edges to represent each segment, then bfs the shortest path

pretty sure this is correct, some sort of technical implemenation bug
might be going on with the code below
"""

class Node:
    def __init__(self):
        self.edges = list()
        self.score = -1

def f(x,inc):
    i = 0
    j = x
    while inc != 1:
        i += 1
        j //= 2
        inc //= 2
    print("? "+str(i)+" "+str(j),flush=True)
    return readint()

def evalRange(n,l,r):
    ans = 0
    for i in range(n):
        if l > r: break
        inc = 2**i
        if l % 2 == 1:
            print("? "+str(i)+" "+str(l),flush=True)
            l += 1
            ans += readint()
        if l > r: break
        if r % 2 == 0:
            print("? "+str(i)+" "+str(r),flush=True)
            r -= 1
            ans += readint()
        if l > r: break
        l //= 2
        r //= 2
    return ans

def qC(n,l,r):
    q = 0
    for i in range(n):
        if l > r: break
        inc = 2**i
        if l % 2 == 1:
            q += 1
            l += 1
        if l > r: break
        if r % 2 == 0:
            q += 1
            r -= 1
        if l > r: break
        l //= 2
        r //= 2
    return q

n,l,r = readints()
r += 1
nodeList = list()
for _ in range(2**n):
    nodeList.append(Node())
nodeList.append(Node())
for nl in range(n):
    xv = 2**nl
    for ii in range(xv,2**n,xv):
        nodeList[ii].edges.append(ii+xv)
        nodeList[ii+xv].edges.append(ii)
nodeList[l].score = 0
nr = [l]
while nodeList[r].score == -1:
    nextr = list()
    for iii in nr:
        for jk in nodeList[iii].edges:
            if nodeList[jk].score == -1:
                nextr.append(jk)
                nodeList[jk].score = nodeList[iii].score + 1
    nr = nextr

# backtrack the path
index = r
queries = list()
while nodeList[index].score != 0:
    for kk in nodeList[index].edges:
        if nodeList[kk].score + 1 == nodeList[index].score:
            queries.append((min(index,kk),max(index,kk)-1))
            index = kk
            break
"""
best = qC(n,l,r)
index = 0
for i in range(1,n):
    inc = 2**i
    lb,rb = (l//inc*inc),((r+inc)//inc*inc-1)
    if lb == 0: lb = l
    if rb > (2**n): rb = r
    c = qC(n,lb,rb)
    if lb != l: c += qC(n,lb,l-1)
    if rb != r: c += qC(n,r+1,rb)
    if best > c:
        c = best
        index = i

# evaluate best option
ans = 0
inc = 2**index
lb,rb = (l//inc*inc),((r+inc)//inc*inc-1)
if lb == 0: lb = l
if rb > (2**n): rb = r
ans = evalRange(n,lb,rb)
if lb != l: ans -= evalRange(n,lb,l-1)
if rb != r: ans -= evalRange(n,r+1,rb)
"""
ans = 0
for snth in queries:
    xx = evalRange(n,snth[0],snth[1])
    if snth[0] < l or snth[1] > r: ans -= xx
    else: ans += xx
print("! "+str(ans % 100),flush=True)
