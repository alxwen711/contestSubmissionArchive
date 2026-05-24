import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
set some prefix to all negatives
then there should exist a singular positive
for sacrificial purpose
any positive value can serve as the sacrifice point
"""

def easypart(ar):
    pos = True
    ans = list()
    n = len(ar)
    for i in range(n-1,-1,-1):
        if pos:
            if ar[i] > 0:
                pos = False
                ans.append(i+1)
        else:
            if ar[i] < 0:
                pos = True
                ans.append(i+1)
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = list()
    best = sum(ar)
    t = best
    index = -1 # sacrifice index
    for i in range(n):
        if ar[i] > 0: # can serve as start point
            v = t-(ar[i]*2)
            if v > best:
                best = v
                index = i 
        if ar[i] < 0:
            t -= 2*ar[i] # pos flip scenario
    if index != -1: # this will NEVER be 0
        ans = easypart(ar[:index])
        ans.append(index+1)
    print(len(ans))
    print(*ans)
        
