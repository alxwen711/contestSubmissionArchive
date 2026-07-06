import sys

def x(a,b,c):
    return c - b + 1
    

for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    #1: o1 only
    diff = b-a
    #2: o3 then o1/2
    ax = x(a,b,a | b)
    
    ans = min(diff,ax)
    #3: set b to optimal
    h = 100000000
    for j in range(ans):
        n = j+1
        w = x(a,(b+n),a|(b+n))+n
        if w > 0:
            h = min(w,h)

    #4: set a to optimal
    r = 1000000000
    for k in range(ans):
        y = x((a+k+1),b,(a+k+1)|b)+k+1
        if y > 0:
            r = min(y,r)
    h = min(r,h)
    print(min(ans,h))
