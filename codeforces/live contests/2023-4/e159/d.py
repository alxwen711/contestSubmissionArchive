import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
offline processing?
track first and last time each spot
is hit in a normal route
0,0 is always assumed to be hit
"""

def move(m,x):
    if m == "U": return (x[0],x[1]+1)
    if m == "D": return (x[0],x[1]-1)
    if m == "L": return (x[0]-1,x[1])
    if m == "R": return (x[0]+1,x[1])
    
def inrange(ar,l,r):
    low = 0
    high = len(ar)-1
    while high-low > 1:
        mid = (low+high)//2
        if l <= ar[mid] <= r: return True
        elif ar[mid] > r: high = mid
        else: low = mid
    if l <= ar[low] <= r: return True
    if l <= ar[high] <= r: return True
    return False
    
n,q = readints()
s = sys.stdin.readline()
normal = [(0,0)]
reverse = [(0,0)]

for i in range(n):
    normal.append(move(s[i],normal[-1]))
    reverse.append(move(s[n-i-1],reverse[-1]))

nd = {}
rd = {}
for j in range(n+1):
    if nd.get(normal[j]) == None: nd[normal[j]] = list()
    nd[normal[j]].append(j)
    if rd.get(reverse[j]) == None: rd[reverse[j]] = list()
    rd[reverse[j]].append(j)

for _ in range(q):
    x,y,l,r = readints()
    ans = "NO"
    if nd.get((x,y)) != None:
        if nd[(x,y)][0] < l or nd[(x,y)][-1] >= r: ans = "YES"
    if ans == "NO": #check mid section
        st = n-r
        ed = n-l+1
        movement = (x-normal[l-1][0],y-normal[l-1][1])
        target = (movement[0]+reverse[st][0],movement[1]+reverse[st][1])
        if rd.get(target) != None: #must be inbetween st and ed
            if inrange(rd[target],st,ed): ans = "YES"
    print(ans)


