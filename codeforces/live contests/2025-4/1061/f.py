import sys
from heapq import *

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy version, O(n^2) will work

x+2 x+1 x -> x x+2 x+1
x+2 x x+1 -> x x+1 x+2

you could try greedy? detect moves in roughly O(1),
there are at most O(n^2) moves that are makeable,
then eject moves that are clearly impossible

bit of a bozo greedy, but really cannot see where this screws up
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    pos = [-1]*(n+1)
    for i in range(n):
        pos[ar[i]] = i
    doable = [0]*(n-1)
    h = list()
    for j in range(1,n-1):
        if pos[j+2] < pos[j] and pos[j+2] < pos[j+1]:
            doable[j] = 1
            h.append(j)
    while len(h) != 0:
        x = heappop(h)
        if pos[x+2] < pos[x] and pos[x+2] < pos[x+1]:
            #print("moving",x)
            pos[x],pos[x+1],pos[x+2] = pos[x+2],pos[x],pos[x+1]
            # check if moved setups can be redone
            for a in range(max(1,x-2),min(x+2,n-2)+1):
                if a != x:
                    if pos[a+2] < pos[a] and pos[a+2] < pos[a+1] and doable[a] == 0:
                        heappush(h,a)
                        doable[a] = 1
        doable[x] = 0
    ans = [0]*n
    for i in range(1,n+1):
        ans[pos[i]] = i
    print(*ans)
