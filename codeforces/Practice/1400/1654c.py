import sys

class queue:
    def __init__(self,limit=100000):
        self.q = list()
        self.pt = 0
        self.l = 0
        self.memRefresh = limit

    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        #check if memory needs to be refreshed
        if self.pt == self.memRefresh:
            self.pt = 0
            self.l -= self.memRefresh
            self.q = self.q[self.memRefresh:]
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self) -> int:
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l

def bs(ar,x):
    high = len(ar)-1
    low = 0
    if high == -1: return -1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] == x: return mid
        elif ar[mid] > x: high = mid
        else: low = mid
    if ar[high] == x: return high
    elif ar[low] == x: return low
    return -1

def freq_dict(ar, pos = False) -> dict:
    d = {}
    if ar == None: return d
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None:
            if pos: d[x] = list()
            else: d[x] = 0
        if pos: d[x].append(i)
        else: d[x] += 1
    return d

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    pieces = queue()
    pieces.add(sum(ar))
    ar.sort()
    d = freq_dict(ar)
    cuts = n-1
    for j in range(cuts):
        x = pieces.dequeue()
        a,b = x//2, (x//2)+(x%2)
        bb = d.get(b)
        if bb != None and bb != 0:
            d[b] -= 1
        else:
            pieces.add(b)
            #if len(pieces) == 0: pieces.append(b)
            #elif b > pieces[0]: pieces.insert(0,b)
            #else: pieces.append(b)
        ba = d.get(a)
        if ba != None and ba != 0:
            d[a] -= 1
        else:
            pieces.add(a)
            #if len(pieces) == 0: pieces.append(a)
            #elif a > pieces[0]: pieces.insert(0,a)
            #else: pieces.append(a)
        #print(pieces)
    
    if cuts == 0 or pieces.length() == 0: print("YES")
    else: print("NO")
    """
        p = list()
        while not pieces.empty():
            p.append(pieces.dequeue())
        p.sort()
        pieces = p
        a = True
        for k in range(len(pieces)):
            if ar[k] != pieces[k]:
                a = False
                break
        if a: print("YES")
        else: print("NO")
"""
