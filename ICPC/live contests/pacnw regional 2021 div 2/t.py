from math import gcd

a,b,n  = map(int,input().split())
n += 1
def countBounces(mgh,a,b):
    hd = mgh*2
    vd = hd*a/b
    v = (vd+1)//2
    return mgh+v
    

lgh = 0
hgh = 2000000
endBounces = 0 #ray ends on bounce x on hor wall if True, ver wall otherwise
hor = False
while hgh - lgh != 1:
    mgh = (lgh+hgh)//2
    tb = countBounces(mgh,a,b)
    if tb == n:
        hor = True
        endBounces = mgh
        #print(mgh)
        break #all conditions met, ending is on a horizontal wall
    elif tb > n: hgh = mgh
    else: lgh = mgh

#print(lgh, hgh)
if not hor:
    if countBounces(lgh,a,b) == n:
        hor = True
        endBounces = lgh
    elif countBounces(hgh,a,b) == n:
        hor = True
        endBounces = hgh
    else:
        remaining = n - countBounces(lgh,a,b)
        endBounces = remaining + countBounces(lgh,a,b) - lgh #total vertical bounces
p,q,r,s = 1,1,1,1

if hor: #ends on horizontal
    hb = int(endBounces)
    vb = int(n - hb)
    if hb % 2 == 0:
        p = -1
    #determine rs
    hd = hb*2
    numer = int(hd*a)
    denom = int(b)
    numer += (3*denom)
    cycles = (numer/denom)//4
    numer -= cycles*4*denom
    if numer <= denom*2: #less or equal to 2
        numer = denom - numer
    else:
        numer = numer - (3*denom)
    #print(numer,denom)
    div = gcd(int(numer),int(denom))
    r = int(numer//div)
    s = int(denom//div)

else: #ends on vertical
    vb = int(endBounces)
    hb = int(n - vb)
    if vb % 2 == 0:
        r = -1
    #determine pq
    vd = vb * 2 - 1
    numer = int(vd*b)
    denom = int(a)
    cycles = (numer/denom)//4
    numer -= cycles*4*denom
    if numer <= denom*2:
        numer -= denom
    else:
        numer = (denom*3) - numer
    #print(numer,denom)
    div = gcd(int(numer),int(denom))
    p = int(numer//div)
    q = int(denom//div)

print(p,q,r,s)
    

