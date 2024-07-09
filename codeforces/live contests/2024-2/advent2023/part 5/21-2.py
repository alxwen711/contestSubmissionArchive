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
"""
part 2


field setups
modulus for non edge cases will remain the same (64, start from corner)
starts with 202298 full sets, even base (101149 odd target, 101149 even)
then subtract odd,even... until no odd, no even (202300 iterations)

each point needs max odd, max even, and even 64 cap, and odd 195 cap
once odd/even 0,0, still add even 64 cap one more time


axis setups
66 steps to get to a new board, 131 to traverse afterwards

202299 full boards used, even base (101150 odd target, 101149 even)
last board needs 130 more steps (even 130 cap)
no additional cap needs to be calculated since second last has 261 steps

center board just use original solver with inf cap

ideally try to make this testable on example input

base is 7344 for input
base is 42 for example input

note that some spots seem to be completely blocked off

605492675373160 is too high, check significantly lower
605102345678912 is too low, in the correct area of values
sample2 results should be (steps+1)**2, base is 4 if odd, 5 if even

quadratic idea finally worked, so somewhere I'm off by 16 for some inexplicable reason
"""

ar = list()
#input, default to basic integer reading file
f = open("21.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()


def track(ar,sx,sy,alim,blim,clim):
    br = list()
    n = len(ar)
    for i in range(n):
        tmp = list()
        for j in range(n):
            tmp.append(-1)
        br.append(tmp)
    br[sx][sy] = 0
    #cr = [(sx,sy)]
    q = queue()
    q.add((sx,sy))
    while not q.empty():
        a = q.dequeue()
        x,y = a[0],a[1]
        v = br[x][y]
        if x != 0:
            if br[x-1][y] == -1 and ar[x-1][y] != "#":
                br[x-1][y] = v + 1
                q.add((x-1,y))
        if x != n-1:
            if br[x+1][y] == -1 and ar[x+1][y] != "#":
                br[x+1][y] = v + 1
                q.add((x+1,y))

        if y != 0:
            if br[x][y-1] == -1 and ar[x][y-1] != "#":
                br[x][y-1] = v + 1
                q.add((x,y-1))

        if y != n-1:
            if br[x][y+1] == -1 and ar[x][y+1] != "#":
                br[x][y+1] = v + 1
                q.add((x,y+1))

    ans = [0,0,0,0,0] #alim, blim, odd max, even max, clim
    for aa in br:
        for ab in aa:
            if ab != -1: #actually reachable
                if ab % 2 == 0: ans[3] += 1
                else: ans[2] += 1
                if (ab % 2) == (alim % 2) and ab <= alim: ans[0] += 1
                if (ab % 2) == (blim % 2) and ab <= blim: ans[1] += 1
                if (ab % 2) == (clim % 2) and ab <= clim: ans[4] += 1
    return ans

"""
13165,149441560
26265,594779360
39365,1336017160
quadratic method is STILL giving too high answer
somewhere in this I am overcounting by a constant
"""
steps = 26501365
n = len(ar)
mid = n//2
ans = 0
base = 7344 #use reference above
print(n,mid)
#determine corner parameters, tl,tr,bl,br
nt = steps-mid-mid-2
fc = (nt//n)-2 #number of FULL boards that can be covered
m = nt % n #b limit, b lowest, then a, then c
print(fc+2,"edges span this many boxes plus some change as",m)
corners = [track(ar,0,0,m+n,m,m+n+n),track(ar,0,n-1,m+n,m,m+n+n),track(ar,n-1,0,m+n,m,m+n+n),track(ar,n-1,n-1,m+n,m,m+n+n)]
odd = fc//2
even = fc//2
st = nt % 2 #0 is even, 1 is odd
if fc % 2 == 1:
    if st == 1: odd += 1
    else: even += 1
for ii in range(fc+1):
    for jj in range(4):
        ans += corners[jj][2]*odd
        ans += corners[jj][3]*even
        ans += corners[jj][0]
        ans += corners[jj][1]
        ans += corners[jj][4]
    if st == 1: odd -= 1
    else: even -= 1
    st ^= 1
print(odd,even) #0,-1 or -1,0

for v in range(4):
    ans += corners[v][1]
    ans += corners[v][1]
    ans += corners[v][0]
    
        
#determine edge parametrs, t,b,l,r
nt = steps-mid-1
fc = (nt//n)-2 #number of FULL boards that can be covered
m = nt % n #b limit
print(fc+2,"edges span this many boxes plus some change as",m)
edges = [track(ar,0,mid,m+n,m,m+n+n),track(ar,n-1,mid,m+n,m,m+n+n),track(ar,mid,0,m+n,m,m+n+n),track(ar,mid,n-1,m+n,m,m+n+n)]
odd = fc//2
even = fc//2
st = nt % 2 #0 is even, 1 is odd
if fc % 2 == 1:
    if st == 1: odd += 1
    else: even += 1
for q in range(4):
    ans += edges[v][2]*odd
    ans += edges[v][3]*even
    ans += edges[v][0]
    ans += edges[v][1]
    ans += edges[v][4]
    
ans += base
print(ans)
