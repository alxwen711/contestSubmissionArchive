import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
super implementation hell

general movement:
if in big, b->s->b->s->b to target
if in small, consider 4 options of moving to/from big
translation diff between big->big needs 45 degree rotational
"""

def dist(ax,ay,bx,by):
    rax = (ax+ay+1)//2
    rbx = (bx+by+1)//2
    ray = ay-rax+1
    rby = by-rbx+1
    #print(rax,ray,rbx,rby)
    return (abs(rax-rbx)+abs(ray-rby))*2

def dist2(ax,ay,bx,by):
    rax = (ax+ay+1)//2
    rbx = (bx+by+1)//2
    ray = ay-rax+1
    rby = by-rbx+1
    #print(rax,ray,rbx,rby)
    d = (abs(rax-rbx)+abs(ray-rby))*2
    p = abs(abs(rax-rbx)-abs(ray-rby))
    ep = abs(rax-rbx)+abs(ray-rby)
    #if ep % 2 == 1: ep -= 1
    d -= (ep-p)//2
    return d

k = readint()
sx,sy = readints()
tx,ty = readints()

ax,ay = sx//k,sy//k
bx,by = tx//k,ty//k

ab = (ax+ay) % 2
bb = (bx+by) % 2
#print(ax,ay,bx,by)
if k == 1: print(abs(sx-tx)+abs(sy-ty))
elif k == 2:
    if ab == 1 and bb == 1: # double big
        print(dist2(ax,ay,bx,by))
    elif ab == 1: # ending small
        options = [dist2(ax,ay,bx,by+1)+(k-(ty % k)), # top
                   dist2(ax,ay,bx,by-1)+(1+(ty % k)), # bot
                   dist2(ax,ay,bx-1,by)+(1+(tx % k)), # left
                   dist2(ax,ay,bx+1,by)+(k-(tx % k))] # right
        print(min(options))
    elif bb == 1: # start small
        options = [dist2(ax,ay+1,bx,by)+(k-(sy % k)), # top
                   dist2(ax,ay-1,bx,by)+(1+(sy % k)), # bot
                   dist2(ax-1,ay,bx,by)+(1+(sx % k)), # left
                   dist2(ax+1,ay,bx,by)+(k-(sx % k))] # right
        print(min(options))
    else: # both small
        options = [dist2(ax,ay+1,bx,by+1)+(k-(ty % k))+(k-(sy % k)), # top
                   dist2(ax,ay-1,bx,by+1)+(k-(ty % k))+(1+(sy % k)), # top
                   dist2(ax-1,ay,bx,by+1)+(k-(ty % k))+(1+(sx % k)), # top
                   dist2(ax+1,ay,bx,by+1)+(k-(ty % k))+(k-(sx % k)), # top
                   dist2(ax,ay+1,bx,by-1)+(1+(ty % k))+(k-(sy % k)), # bot
                   dist2(ax,ay-1,bx,by-1)+(1+(ty % k))+(1+(sy % k)), # bot
                   dist2(ax-1,ay,bx,by-1)+(1+(ty % k))+(1+(sx % k)), # bot
                   dist2(ax+1,ay,bx,by-1)+(1+(ty % k))+(k-(sx % k)), # bot
                   dist2(ax,ay+1,bx-1,by)+(1+(tx % k))+(k-(sy % k)), # left
                   dist2(ax,ay-1,bx-1,by)+(1+(tx % k))+(1+(sy % k)), # left
                   dist2(ax-1,ay,bx-1,by)+(1+(tx % k))+(1+(sx % k)), # left
                   dist2(ax+1,ay,bx-1,by)+(1+(tx % k))+(k-(sx % k)), # left
                   dist2(ax,ay+1,bx+1,by)+(k-(tx % k))+(k-(sy % k)), # right
                   dist2(ax,ay-1,bx+1,by)+(k-(tx % k))+(1+(sy % k)), # right
                   dist2(ax-1,ay,bx+1,by)+(k-(tx % k))+(1+(sx % k)), # right
                   dist2(ax+1,ay,bx+1,by)+(k-(tx % k))+(k-(sx % k))] # right
        print(min(options))
elif ab == 1 and bb == 1: # double big
    print(dist(ax,ay,bx,by))
elif ab == 1: # ending small
    options = [dist(ax,ay,bx,by+1)+(k-(ty % k)), # top
               dist(ax,ay,bx,by-1)+(1+(ty % k)), # bot
               dist(ax,ay,bx-1,by)+(1+(tx % k)), # left
               dist(ax,ay,bx+1,by)+(k-(tx % k))] # right
    print(min(options))
elif bb == 1: # start small
    options = [dist(ax,ay+1,bx,by)+(k-(sy % k)), # top
               dist(ax,ay-1,bx,by)+(1+(sy % k)), # bot
               dist(ax-1,ay,bx,by)+(1+(sx % k)), # left
               dist(ax+1,ay,bx,by)+(k-(sx % k))] # right
    print(min(options))
else: # both small
    options = [dist(ax,ay+1,bx,by+1)+(k-(ty % k))+(k-(sy % k)), # top
               dist(ax,ay-1,bx,by+1)+(k-(ty % k))+(1+(sy % k)), # top
               dist(ax-1,ay,bx,by+1)+(k-(ty % k))+(1+(sx % k)), # top
               dist(ax+1,ay,bx,by+1)+(k-(ty % k))+(k-(sx % k)), # top
               dist(ax,ay+1,bx,by-1)+(1+(ty % k))+(k-(sy % k)), # bot
               dist(ax,ay-1,bx,by-1)+(1+(ty % k))+(1+(sy % k)), # bot
               dist(ax-1,ay,bx,by-1)+(1+(ty % k))+(1+(sx % k)), # bot
               dist(ax+1,ay,bx,by-1)+(1+(ty % k))+(k-(sx % k)), # bot
               dist(ax,ay+1,bx-1,by)+(1+(tx % k))+(k-(sy % k)), # left
               dist(ax,ay-1,bx-1,by)+(1+(tx % k))+(1+(sy % k)), # left
               dist(ax-1,ay,bx-1,by)+(1+(tx % k))+(1+(sx % k)), # left
               dist(ax+1,ay,bx-1,by)+(1+(tx % k))+(k-(sx % k)), # left
               dist(ax,ay+1,bx+1,by)+(k-(tx % k))+(k-(sy % k)), # right
               dist(ax,ay-1,bx+1,by)+(k-(tx % k))+(1+(sy % k)), # right
               dist(ax-1,ay,bx+1,by)+(k-(tx % k))+(1+(sx % k)), # right
               dist(ax+1,ay,bx+1,by)+(k-(tx % k))+(k-(sx % k))] # right
    print(min(options))

    
