import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
must be even length to be good and have same 0/1 count
find last 1, start from there
if starting with 0, set left as entire segment until the last 1
otherwise, set entire right segment from the first 0

if even len and same 0/1, it's possible (following method is fast enough?)
go inwards to the string
if 0 0, place 01 right to right fault
if 1 1, place 01 left of left fault
naively this is O(n^2)
"""

def solve(n,s):
    one,zero = 0,0
    ar = list()
    for i in range(n):
        if s[i] == "0": zero += 1
        else: one += 1
        ar.append(int(s[i]))
    if one != zero:
        print(-1)
        return
    #this is possible
    l = 0
    r = len(ar)-1
    ans = list()
    while l < r:
        if ar[l] != ar[r]:
            l += 1
            r -= 1
        elif ar[l] == 0: #0 fault
            r += 1
            ans.append(r)
            ar.insert(r,0)
            ar.insert(r+1,1)
            l = 0
            r = len(ar)-1
        else: #1 fault
            ans.append(l)
            ar.insert(l,1)
            ar.insert(l,0)
            l = 0
            r = len(ar)-1
    print(len(ans))
    print(*ans)
    return
            
    
for _ in range(readint()):
    n = readint()
    s = input()
    solve(n,s)
    
