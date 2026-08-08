import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the valid point should be such where the ship is not destroyed?
yes because due to the 4th test case, something like (5,5) is
possible with XYYX but this is outside boundary

regardless of X/Y, move setup is 1,2,3,4,5,6,7,8...

then the goal is to determine the maximum steps possible
which determines what point exactly is possible
then solve for the X positions in the array
"""

for _ in range(readint()):
    x,y = readints()
    low = 1 # always possible
    high = 21000 # always impossible
    while high-low > 1:
        mid = (low+high)//2
        if (mid*mid+mid)//2 > (x+y): high = mid
        else: low = mid
    ans = ["Y"]*low
    dist = (low*low+low)//2
    diff = x+y-dist
    tx,ty = x-(diff//2),y-((diff+1)//2)
    if tx < 0:
        ty += tx
        tx = 0
    if ty < 0:
        tx += ty
        ty = 0
    # now solve for tx
    for i in range(low):
        if tx == 0: break
        if tx > (low-i):
            ans[i] = "X"
            tx -= (low-i)
        else:
            ans[-tx] = "X"
            break
    print(*ans,sep="")
