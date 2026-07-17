import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
3n spots must be filled
every spot is filled in n = 3
ABC
BCA
CAB

.....
.....
.....
.....
.....


.ABC
CB.A
BCA.
A.CB
"""

class state:
    def __init__(self,prev,step,score):
        self.ar = list()
        self.s = step+1 #how many filled in
        self.f = score
        for snth in prev:
            self.ar.append(snth)

def rsearch(n,ar,index,m):
    for i in range(m):
        if ar[n*index+i] != ".": return ar[n*index+i]
    return "."

def csearch(n,ar,index,m):
    for i in range(m):
        if ar[n*i+index] != ".": return ar[n*i+index]
    return "."

def nsearch(n,ar,r,c,x):
    for a in range(n):
        if ar[n*r+a] == x: return False
    for b in range(n):
        if ar[n*b+c] == x: return False
    return True

def f(n,ar,br):
    base = state(['.']*(n*n),-1,0)
    sl = [base]
    ch = ["A","B","C"]
    while len(sl) != 0:
        x = sl.pop()
        r = 3*n-x.f
        if r == 0:
            print("Yes")
            for nn in range(n):
                ans = x.ar[(n*nn):(n*(nn+1))]
                print(*ans,sep="")
            return
        if (n*n-x.s) > r: #can blank
            sl.append(state(x.ar,x.s,x.f))
        pos = x.s
        rv = rsearch(n,x.ar,pos//n,pos%n) 
        cv = csearch(n,x.ar,pos%n,pos//n)
        for i in ch:
            if nsearch(n,x.ar,pos//n,pos%n,i): #clear unique pos
                rrv = rv
                ccv = cv
                if rrv == ".": rrv = i
                if ccv == ".": ccv = i
                if rrv == ar[pos//n] and ccv == br[pos%n]: #clear first pos
                    ns = state(x.ar,x.s,x.f+1)
                    ns.ar[pos] = i
                    sl.append(ns)
    print("No")
                    
            

        
n = readint()
ar = input()
br = input()

f(n,ar,br)
