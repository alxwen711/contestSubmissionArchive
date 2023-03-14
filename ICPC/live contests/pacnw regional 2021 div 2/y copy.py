from math import sqrt
from decimal import *
"""def l(m,n): #len between two points
    return sqrt(((m[0]-n[0])*(m[0]-n[0]))+((m[1]-n[1])*(m[1]-n[1])))
"""
# attempting to upsolve this

def triangle(a,b,c): # area of 3 points
    """x,y,z = l(a,b), l(b,c), l(a,c)
    s = (x+y+z)/2
    return sqrt(s*abs(s-x)*abs(s-y)*abs(s-z))
"""
    sum1 = a[0]*b[1]+b[0]*c[1]+c[0]*a[1]
    sum2 = a[1]*b[0]+b[1]*c[0]+c[1]*a[0]
    return abs(sum1-sum2)/2
     
points = list()
n = int(input())
for i in range(n):
    tmp = list()
    a,b = map(Decimal,input().split())
    tmp.append(a)
    tmp.append(b)
    points.append(tmp)


area = 0
for j in range(n-2):
    area += triangle(points[0],points[j+1],points[j+2])
    #print(area)
target = area/2
carea = 0
stop = 0
for k in range(n-2):
    carea += triangle(points[0],points[k+1],points[k+2])
    if carea > target:
        carea -= triangle(points[0],points[k+1],points[k+2])
        stop = k
        break

remaining = target-carea
aa = points[stop+1]
ab = points[stop+2]
mid = list()
mid.append((points[stop+1][0]+points[stop+2][0])/2)
mid.append((points[stop+1][1]+points[stop+2][1])/2)
for i in range(2727):
    mid[0] = (aa[0]+ab[0])/2
    mid[1] = (aa[1]+ab[1])/2
    #print(aa,ab,mid)
    last = triangle(points[0],points[stop+1],mid)
    if last >= remaining:
        ab[0] = mid[0]
        ab[1] = mid[1]
    elif last < remaining:
        aa[0] = mid[0]
        aa[1] = mid[1]
    """
last = triangle(points[0],points[stop+1],points[stop+2])
crit = 0
if last != 0: crit = remaining/last
aa = points[stop+1][0]*(1-crit)+points[stop+2][0]*crit
ab = points[stop+1][1]*(1-crit)+points[stop+2][1]*crit
print("%.10f" % aa, "%.10f" % ab)
"""
ansa = Decimal("%.7f" % mid[0]).normalize()
ansb = Decimal("%.7f" % mid[1]).normalize()

print(ansa,ansb)   
#print("%.10f" % mid[0], "%.10f" % mid[1])
