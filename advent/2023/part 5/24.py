"""
6188 is too low?
4287 after bug fix
20361 for part 1


AFTER some amount of time t, there will be for EVERY equation a UNIQUE t where:

a+tx = ai+txi
b+ty = bi+tyi
c+tz = ci+tzi

if it's anything 448 is too low for part 2

fix the entire graph to the first hailstone (point 1 acts at origin and does not move, all other points are adjusted relative)
2nd hailstone creates a line the rock must intersect, get the plane that is based on the line and intersects the origin

get the points and times where 3rd/4th hailstone intersect the plane, this is the rock line's slope and times
from above info get starting point (time 0)
confirm this path crosses the origin, then revert the mapping to standard (unfix first hailstone as origin)
"""

class Line:
    def __init__(self,ar,br):
        self.p = ar
        self.v = br


def parameters(i):
    p,v = i.split("@")
    ar = list(map(int,p.split(",")))
    br = list(map(int,v.split(",")))
    return ar,br


def collide(a,b): #check if two lines collide, and if so, when
    if a.v[1]*b.v[0] == a.v[0]*b.v[1]: return -1,-1,-1 #impossible
    aslope = a.v[1]/a.v[0]
    bslope = b.v[1]/b.v[0]
    

    #line up x-coordinate with a
    dist = a.p[0]-b.p[0]
    by = b.p[1]+bslope*dist

    #determine x/y intersection
    dslope = aslope-bslope #1 x movement, change between a and b
    target = by-a.p[1]
    xint = a.p[0]+(target/dslope)
    yint = a.p[1]+(target/dslope)*aslope

    #determine if this is actually valid for both
    if xint > b.p[0] and b.v[0] < 0: return -1,-1,-1
    elif xint < b.p[0] and b.v[0] > 0: return -1,-1,-1
    if xint > a.p[0] and a.v[0] < 0: return -1,-1,-1
    elif xint < a.p[0] and a.v[0] > 0: return -1,-1,-1

    #print(xint,yint,a.p,b.p)
    #determine if z factor is at least close enough
    az = a.p[2]+(target/dslope)*(a.v[2]/a.v[0])
    bz = b.p[2]+(xint-b.p[0])*(b.v[2]/b.v[0])
    if abs(az-bz) < 0.000001: return xint,yint,az
    return xint,yint,-1

    
ar = list()
#input, default to basic integer reading file
f = open("24.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

lines = list()
for i in ar:
    a,b = parameters(i)
    lines.append(Line(a,b))

print(lines[0].p)
print(lines[0].v)
n = len(lines)
print(n)

ans = 0
count = 0
for c in range(n-1):
    for d in range(c+1,n):
        count += 1
        cx,cy,cz = collide(lines[c],lines[d])
        if min(cx,cy) >= 200000000000000 and max(cx,cy) <= 400000000000000: ans += 1
print(ans)
print(count)
