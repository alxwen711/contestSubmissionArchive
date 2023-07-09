import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
first determine how much beauty each row can give for amount
then bin search for num of full rows
then create last partial filled row
take each segment length, fill greedily? (can skip 1 cells)

greedily count max amount of segments of each length, fill
from largest section to smallest
build seg length count from reverse down?
upon adding a new position, check left and right spots to see
if connecting, use a class structure to keep track of segment
lengths, add/remove as needed, also need a dict setup to track
the frequencies of each possible segment length, add the present
seg lengths as needed, at worst there are sqrt(200000) that are used
in theory this would end up as a O(n sqrt n) algorithm??
In practice this is probably lower than 80 mill operations
this problem will be upsolved with this idea since I'm not implementing
this in 10 minutes
"""

class nonZeroAr:
    def __init__(self,n):
        self.ar = [0]*(n+1) #freq of each segment length
        self.present = set() #current freqencies in set
    
    def add(self,x):
        if self.ar[x] == 0: self.present.add(x)
        self.ar[x] += 1

    def sub(self,x):
        if self.ar[x] == 1: self.present.discard(x)
        self.ar[x] -= 1
    

def solve(n,ar,m):
    d = {}
    for i in range(n):
        x = ar[i]
        if d.get(x) == None: d[x] = list()
        d[x].append(i)
    freq = nonZeroAr(n) 
    total = [0]*(n+1) #total freq (only need 2+)
    l = [-1]*n #left endpoints of segments with here as right boundary
    r = [-1]*n #right endpoints of segments with here as left boundary
    for j in range(n):
        if d.get(j) != None: #add elements from this row
            for v in d[j]:
                le = False
                re = False
                if v == n-1: re = True
                elif r[v+1] == -1: re = True
                if v == 0: le = True
                elif l[v-1] == -1: le = True
                if le and re: #empty island
                    l[v] = v
                    r[v] = v
                    freq.add(1)
                elif le: #only left point included
                    b = r[v+1]
                    length = b-v
                    freq.sub(length)
                    freq.add(length+1)
                    l[b] = v
                    r[v] = b
                    r[v+1] = -1
                elif re: #only right point
                    a = l[v-1]
                    length = v-a
                    freq.sub(length)
                    freq.add(length+1)
                    l[v] = a
                    r[a] = v
                    l[v-1] = -1
                else: #merge two segments
                    a = l[v-1]
                    b = r[v+1]
                    nl = b-a+1
                    freq.sub(v-a)
                    freq.sub(b-v)
                    freq.add(nl)
                    r[a] = b
                    l[b] = a
                    l[v-1] = -1
                    r[v+1] = -1
                #print(v,freq.ar)
                
        # update from present
        for k in freq.present:
            total[k] += freq.ar[k]
    #freq contains number of segments of each length
    #fill longest to shortest (only have to go up to len 2)
    ans = 0
    index = n
    for u in range(n-1):
        #determine if index length is doable
        complete = index*total[index]
        if m >= complete:
            m -= complete
            ans += (index-1)*total[index]
        else:
            #if not, last length
            rc = m // index
            r = m % index
            ans += (index-1)*rc
            ans += max(0,r-1)
            break
        index -= 1
    return ans
    

for i in range(readint()):
    n = readint()
    ar = readar()
    m = readint()
    print(solve(n,ar,m))
