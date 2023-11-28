import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
check if O is in a circle
check if P is in a circle
if in same circle, then check if intersect
"""

def dist(a,b,c,d):
    return abs(a-c)**2+abs(b-d)**2

for i in range(readint()):
    px,py = readints()
    ax,ay = readints()
    bx,by = readints()
    cd = (abs(ax-bx)**2+abs(ay-by)**2)/4
    oa = dist(0,0,ax,ay)
    ob = dist(0,0,bx,by)
    pa = dist(px,py,ax,ay)
    pb = dist(px,py,bx,by)
    ansa = max(oa,pa)
    ansb = max(ob,pb)
    ansc = max(cd,oa,pb)
    ansd = max(cd,ob,pa)
    print(min(ansa,ansb,ansc,ansd)**0.5)
