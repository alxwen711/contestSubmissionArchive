import sys
from math import radians,tan,sqrt

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def intersect(a,b,c,d):
    # lines are a to b, c to d, determine if there is intersection
    if a[0] == b[0]: # first line is vertical
        if c[0] > d[0]: c,d = d,c
        if c[0] <= a[0] and d[0] >= a[0]:
            # find the collision point
            if c[0] == d[0]: # also vertical
                if min(c[1],d[1]) > max(a[1],b[1]): return False
                if max(c[1],d[1]) < min(a[1],b[1]): return False
                return True
            else:
                dist = a[0]-c[0]
                vert = d[1]-c[1]
                p = c[1]+vert*(dist/(d[0]-c[0]))
                if p <= max(a[1],b[1]) and p >= min(a[1],b[1]): return True
                return False
        else: return False
    if c[0] == d[0]: return intersect(c,d,a,b)

    # neither line is vertical, use some horizontal checking
    if a[0] > b[0]: a,b = b,a
    if c[0] > d[0]: c,d = d,c

    lowx = max(a[0],c[0])
    highx = min(b[0],d[0])
    if lowx > highx: return False # no horizontal overlap

    # determine y positions at lowx and highx
    vert1 = b[1]-a[1]
    vert2 = d[1]-c[1]
    ay = a[1]+vert1*((lowx-a[0])/(b[0]-a[0]))
    cy = c[1]+vert2*((lowx-c[0])/(d[0]-c[0]))
    lowx_swap = False
    if ay >= cy: lowx_swap = True

    ay = a[1]+vert1*((highx-a[0])/(b[0]-a[0]))
    cy = c[1]+vert2*((highx-c[0])/(d[0]-c[0]))
    highx_swap = False
    if ay >= cy: highx_swap = True

    return lowx_swap ^ highx_swap


def triangle(a,b,c):
    return (a[0]*b[1]-a[1]*b[0]+b[0]*c[1]-b[1]*c[0]+c[0]*a[1]-c[1]*a[0])

def cross(ax,ay,p,q):
    #xx = (p[0]-ax,p[1]-ay)
    #yy = (q[0]-ax,q[1]-ay)

    xx = p[0]-ax
    xy = p[1]-ay
    yx = q[0]-ax
    yy = q[1]-ay
    
    return xx*yy - xy*yx

def inPolygon(trap, px,py):
    n = 4
    cnt = 0
    for i in range(4):
        q = trap[(i + 1) % n]
        cnt ^= ((py<trap[i][1]) - (py < q[1])) * cross(px,py,trap[i],q) > 0
    return cnt > 0

def contained(trap,isle,traparea):
    # ensure that each line segment from trap and each line segment
    # from isle do NOT intersect
    nn = len(isle)
    for i in range(nn):
        for j in range(4):
            if intersect(isle[i],isle[(i+1)%nn],trap[j],trap[(j+1)%4]): return False


    # determine if the first island point is in the trapezoid
    return inPolygon(trap,isle[0][0],isle[0][1])
    

def test_func(n,m,islands,flights,ratio):
    # for each flight, determine the trapezoid
    trapezoids = list()
    areas = list()
    for f in flights:
        # deterimne a vector for the line
        x_diff = f[3]-f[0]
        y_diff = f[4]-f[1]
        distance = sqrt(x_diff*x_diff+y_diff*y_diff)

        # rotate 90 degrees both directions to a unit vector
        left_mag = (-y_diff,x_diff)
        right_mag = (y_diff,-x_diff)

        # compute start and end magnitudes
        start_ratio = f[2]*ratio/distance
        end_ratio = f[5]*ratio/distance
        # -90 start, -90 end, 90 end, 90 start for point order
        pt1 = left_mag[0]*start_ratio+f[0],left_mag[1]*start_ratio+f[1]
        pt2 = left_mag[0]*end_ratio+f[3],left_mag[1]*end_ratio+f[4]
        pt3 = right_mag[0]*end_ratio+f[3],right_mag[1]*end_ratio+f[4]
        pt4 = right_mag[0]*start_ratio+f[0],right_mag[1]*start_ratio+f[1]
        trapezoids.append((pt1,pt2,pt3,pt4))
        areas.append((f[2]+f[5])*2*distance*ratio)
    # then iterate through the islands
    remain = n
    h = [1]*n
    ti = 0
    for t in trapezoids:
        for i in range(n):
            if h[i]:
                # run encapsulation test
                if contained(t,islands[i],areas[ti]):
                    h[i] = 0
                    remain -= 1
                    if remain == 0: return True
        ti += 1
    return False

n,m = readints()
islands = list()
for _ in range(n):
    pts = list()
    for _ in  range(readint()):
        x,y = readints()
        pts.append((x,y))
    islands.append(pts)

flights = list()
for _ in range(m):
    a,b,c,d,e,f = readints()
    flights.append((a,b,c,d,e,f)) # x1,y1,z1,x2,y2,z2


low = 0
high = 90
solved = False
for _ in range(23):
    mid = (low+high)/2
    if test_func(n,m,islands,flights,tan(radians(mid))):
        high = mid
        solved = True
    else: low = mid
    #print(low,high,tan(radians(mid)))

if solved: print((low+high)/2)
else: print("impossible")
