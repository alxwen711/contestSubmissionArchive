import sys
from math import gcd

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    front = list()
    back = list()
    front.append(0)
    back.append(0)
    for j in range(n):
        front.append(gcd(front[-1],ar[j]))
        back.append(gcd(back[-1],ar[-j-1]))
    ans = front[n] #every element, no discount
    ans = max(ans,gcd(back[n-1],br[0]))
    ans = max(ans,gcd(front[n-1],br[-1]))
    for k in range(1,n-1):
        ans = max(ans,gcd(front[k],br[k],back[n-k-1]))
    print(ans)
        
