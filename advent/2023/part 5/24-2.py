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

update: yea this problem is pain, solution below will involve dimensional shifting and plane algebra
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

# start solving here

firstpt = lines[0]
lines[0] = Line([0,0,0],[0,0,0]) #replace with nil line
for j in range(1,n):
    lines[j].p = [lines[j].p[0]-firstpt.p[0],lines[j].p[1]-firstpt.p[1],lines[j].p[2]-firstpt.p[2]]
    lines[j].v = [lines[j].v[0]-firstpt.v[0],lines[j].v[1]-firstpt.v[1],lines[j].v[2]-firstpt.v[2]]

# second line get two points, with origin, create the plane
#from two non origin points, those are vectors
#take cross product of the vectors to get norm (plane equation)
#k = 0 because (0,0,0) is in this plane
    """
    3   3
    0   3
    -3  3
    """
itisfricked = 1
#determine when two other lines cross this plane and where 
#(https://math.libretexts.org/Bookshelves/Calculus/Supplemental_Modules_(Calculus)/Multivariable_Calculus/1%3A_Vectors_in_Space/Intersection_of_a_Line_and_a_Plane)
#extrapolate from the times given to get the starting point (pray this is an integer tuple)
#retranslate back to normal from first point (add pos and vel)
"""
notes for math section, because I want to just get to the finish line already


Starting 4 points
230027994633462, 224850233272831, 164872865225455 @ 103, -57, 285
213762157019377, 204038908928791, 198113097692531 @ 184, -110, 174
236440979253526, 104012423941037, 223798957622735 @ 15, 694, -277
150273374343556, 50901286038655, 131546537769893 @ 272, 413, 324


After translating 1st point:
0,0,0 @ 0,0,0
-16265837614085, -20811324344040, 33240232467076 @ 81, -53, -111
6412984620064, -120837809331794, 58926092397280 @ -88, 751, -562
-79754620289906, -173948947234176, -33326327455562 @ 169, 470, 39

plane is determined by vectors (-16265837614085, -20811324344040, 33240232467076) and (-16265837614004, -20811324344093, 33240232466965)

cross product of vectors is (4071789322943468,886950854669721,2547806665413745),
divide by gcd to get (38108, 8301, 23845) -> 38108x + 8301y + 23845z = 0 (point (0,0,0) must be on this plane)

determine when 3rd/4th point cross this plane, and where
38108*(6412984620064-88*t) + 8301*(-120837809331794+751*t) + 23845*(58926092397280-562*t) = 0
t = 61443247226
pos at t: (1005978864176, -74693930665068, 24394987456268)

38108*(-79754620289906+169*t) + 8301*(-173948947234176+470*t) + 23845*(-33326327455562+39*t) = 0
t = 468244925682
pos at t: (-621227849648, 46126167836364, -15064775353964)

travel distance: (-1627206713824, 120820098501432, -39459762810232)
in 406801678456 nanoseconds

per nanosecond, velocity is (-4, 297, -97)

pos at t = 61443247226: (1005978864176, -74693930665068, 24394987456268)
thus pos at t = 0: (1251751853080, -92942575091190, 30354982437190)
retranslate from first point, start pos is: (231279746486542, 131907658181641, 195227847662645)
sum is: 558415252330828
"""
