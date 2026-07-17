import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
#pr = lambda n: sys.stdout.write(str(n)+'\n')
"""
u,p -> database u, page p
return location from 1 to q
start with initial brute force solution
"""

class queue:
    def __init__(self):
        self.q = list()
        self.pt = 0
        self.l = 0
        self.skip = {} # indicies to skip

    def add(self,x) -> int:
        self.q.append(x)
        self.l += 1
        return self.l-1 #index where this value was located

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        while self.skip.get(self.pt) == 1: self.pt += 1
        return x

    def dequeuei(self,index): # dequeue at index specified, assume that this actually exists
       self.skip[index] = 1
       return self.q[index]

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]
    
    def length(self) -> int: # do not use
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l
    
#def heap: implement if queue method is working

    
class tenant:
    #if space available, add, track last usage date
    #else determine optimal removal by last used (also req dict)
    #check if allowed to remove
    #check if possible to express as two seperate linked int queues
    
    def __init__(self,ml,mb,mh):
        #memory limits
        self.ml = ml
        self.mb = mb
        self.mh = mh

        # everything else
        self.q = queue() # store page stored and time
        self.mu = 0
        self.d = [-1]*100001
        self.i = [-1]*100001 # index of page p in the queue
        
    def find(self,x): #check if page x is already loaded, and where in memory
        return self.d[x]

    def add(self,p,q,t): # page p is added in q in database at time t
        self.mu += 1
        self.d[p] = q
        loc = self.q.add((p,t))
        self.i[p] = loc

    def rem(self): # earliest page is removed as needed, return index of freed mem
        x = self.q.dequeue()
        freepage = self.d[x[0]]
        self.d[x[0]] = -1
        self.mu -= 1
        return freepage

    def mincap(self): # return if at least min pages are actually allocated
        return self.q.top()[0] != 0


    def getTime(self): # return time of earliest page loaded
        return self.q.top()[1]

    def update(self,p,q,t): # update last time page was used
        n = self.i[p]
        if n == self.q.pt: #standard add/remove
            self.rem()
            self.add(p,q,t)
        else: # index remove
            self.q.dequeuei(n)
            self.i[p] = self.q.add((p,t))

# if __name__ == "__main__":
n,q,m = readints()
ar = readar()
br = readar()
cr = readar() #qmin,qbase,qmax
pt = 0
alloc = 0
#  init tenant info
tenants = list()
for sn in range(n):
    tenants.append(tenant(cr[3*sn],cr[3*sn+1],cr[3*sn+2]))
    for u in range(cr[3*sn]):
        tenants[sn].add(0,-1,-1) # make sure each one has at least min space
        alloc += 1

for i in range(m):
    a,b = readints()
    a -= 1
    t = tenants[a]
    page = t.find(b)
    if page == -1: #need to upload page
        placed = False
        if pt != q:
            if not t.mincap(): # can upload to dummy slot
                pt += 1
                t.rem() # remove dummy slot
                t.add(b,pt,i)
                sys.stdout.write(str(pt)+'\n')
                flush()
                placed = True
            elif t.mu != t.mh and alloc != q: # can upload to new slot
                pt += 1
                t.add(b,pt,i)
                sys.stdout.write(str(pt)+'\n')
                flush()
                placed = True
                alloc += 1

                
        if not placed: #must replace "earliest" (loaded, needs to be heap for used)
            bi = -1 # best index
            time = 99999999999999999999
            for j in range(n):
                if (j == a) or (tenants[j].mu > tenants[j].ml): # possible
                    nth = tenants[j].getTime()
                    if nth < time: 
                        time = nth
                        bi = j
            # rem from bi, add to a
            x = tenants[bi].rem()
            t.add(b,x,i)
            sys.stdout.write(str(x)+'\n')
            flush()
    else: # already loaded
        sys.stdout.write(str(page)+'\n')
        flush()
        t.update(b,page,i)
    
