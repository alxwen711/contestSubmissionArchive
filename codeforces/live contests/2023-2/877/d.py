import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
walkable if:
already balanced
if sum is even and ((/)) can be used to fix (ie. even length)
still has to start with ( and end with )
if too high then can use )) to lower segment from end to last pt
where entire section has end pt as min val
if too low then earlist (( has to be before first neg section
no min points below finish, ie. reversal never goes neg
start with (, end with )
first (( appears before ))
last )) appears after ((
if only (( or )), impossible
if neither (( or )), and start/end rule clears, yes
"""

def solve(n,q,s):
    if n % 2 == 1:
        for nsh in range(q):
            readint()
            print("NO")
        return
    arr = list()
    for i in range(n):
        if s[i] == "(": arr.append(1)
        else: arr.append(0)
    ar = list() #first ((
    br = list() #first ))
    cr = list() #last ((
    dr = list() #last ))
    for j in range(n-1):
        x = arr[j]+arr[j+1]
        if x == 2:
            heappush(ar,j)
            heappush(cr,-j)
        elif x == 0:
            heappush(br,j)
            heappush(dr,-j)
    #print(arr)
    #print(ar,br,cr,dr)
    for k in range(q):
        x = readint()
        x -= 1
        arr[x] = arr[x] ^ 1
        if x != 0:
            c = arr[x]+arr[x-1]
            if c == 2:
                heappush(ar,x-1)
                heappush(cr,-(x-1))
            elif c == 0:
                heappush(br,x-1)
                heappush(dr,-(x-1))
        if x != n-1:
            c = arr[x]+arr[x+1]
            if c == 2:
                heappush(ar,x)
                heappush(cr,-x)
            elif c == 0:
                heappush(br,x)
                heappush(dr,-x)
        #update heaps
        while len(ar) != 0:
            if arr[ar[0]]+arr[ar[0]+1] != 2: heappop(ar)
            else: break
        while len(br) != 0:
            if arr[br[0]]+arr[br[0]+1] != 0: heappop(br)
            else: break
        while len(cr) != 0:
            ca = -cr[0]
            if arr[ca]+arr[ca+1] != 2: heappop(cr)
            else: break
        while len(dr) != 0:
            da = -dr[0]
            if arr[da]+arr[da+1] != 0: heappop(dr)
            else: break
        #print(arr)
        #print(ar,br,cr,dr)
        # run tests here
        if arr[0] != 1 or arr[-1] != 0: print("NO")
        elif len(ar)+len(br) == 0: print("YES")
        elif len(ar) == 0 or len(br) == 0: print("NO")
        elif ar[0] < br[0] and cr[0] > dr[0]: print("YES")
        else: print("NO")
        
        
    


n,q = readints()
s = input()
solve(n,q,s)
