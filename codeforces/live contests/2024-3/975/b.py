import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if 1 -> must start there
adjacent 2 -> must start in a 2
3 spots -> requires chain of 3 3's
whatever the minimum value is -> maximum possible starting spots

an endpoint must have a max value, else 0
also having more than k spots with max value k -> 0
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    a = 0
    b = n-1
    for i in range(n):
        a = max(a,i-ar[i]+1)
        b = min(b,i+ar[i]-1)
        br.append((ar[i],i))
    ans = max(0,b-a+1)
    # run null test
    br.sort()
    flag = True
    a,b = 999999999999999,-99999999999
    for j in range(n):
        a,b = min(a,br[j][1]),max(b,br[j][1])
        if b-a+1 > br[j][0]:
            flag = False
            break
    if flag: print(ans)
    else: print(0)
