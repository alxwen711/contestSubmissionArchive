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
part 1
not 3659?

part 2
how many spots exactly 1,3,5,7,9...26501365 steps away
notice the paths for S's vertical/horizontal lines
can be fully traversed (in the clear)

new new plan, run larger and larger grids to try and get a
quadratic formula of some sort
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
print(len(ar),len(ar[0]),len(ar[-1]))


def solve(ar,steps):
    br = list()
    sx,sy = -1,-1
    n = len(ar)
    hv = 0
    for i in range(n):
        tmp = list()
        for j in range(n):
            if ar[i][j] == "S":
                sx,sy = i,j
                tmp.append(0)
            else:
                tmp.append(-1)
                if ar[i][j] == "#": hv += 1
        br.append(tmp)
    #cr = [(sx,sy)]
    q = queue()
    q.add((sx,sy))
    while not q.empty():
        a = q.dequeue()
        x,y = a[0],a[1]
        v = br[x][y]
        if x != 0:
            if br[x-1][y] == -1 and ar[x-1][y] == ".":
                br[x-1][y] = v + 1
                q.add((x-1,y))
        if x != n-1:
            if br[x+1][y] == -1 and ar[x+1][y] == ".":
                br[x+1][y] = v + 1
                q.add((x+1,y))

        if y != 0:
            if br[x][y-1] == -1 and ar[x][y-1] == ".":
                br[x][y-1] = v + 1
                q.add((x,y-1))

        if y != n-1:
            if br[x][y+1] == -1 and ar[x][y+1] == ".":
                br[x][y+1] = v + 1
                q.add((x,y+1))

    ans = 0
    impossible = 0
    for aa in br:
        for ab in aa:
            if ab % 2 == (steps % 2) and ab <= steps and ab >= 0: ans += 1
            if ab == -1: impossible += 1
    return ans

def supergen(ar,x):
    br = list()
    n = len(ar)
    for i in range(n*x):
        row = ar[i % n]
        tmp = list()
        for j in range(x):
            for k in range(n):
                if row[k] == "#": tmp.append("#")
                else: tmp.append(".")
        br.append(tmp)
    m = len(br)
    br[m//2][m//2] = "S"
    return br

print(solve(ar,64)) #initial test to make sure this works as intended

nn = len(ar)
for z in range(1,11):
    cr = supergen(ar,z*2-1)
    s = 65+(nn*(z-1))
    print(s,solve(cr,s))



