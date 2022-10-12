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
    ans = "YES"
    for j in range(n-2):
        x,y = (ar[j]*ar[j+1])//gcd(ar[j],ar[j+1]),(ar[j+1]*ar[j+2])//gcd(ar[j+1],ar[j+2])
        if gcd(x,y) != ar[j+1]:
            ans = "NO"
            break
    """
this mess really cost me 2400 ranks in the contest
    for j in range(n-2):
        if ar[j] > ar[j+1] and ar[j+1] < ar[j+2] and ar[j+2] % ar[j+1] == 0 and ar[j] % ar[j+1] == 0:
            ans = "NO"
            break
    #1 test (even,odd # of 1s,even)
    
    st = -1
    ed = -1
    inset = True
    for k in range(n):
        if inset:
            if ar[k] % 2 != 1:
                ed = k
                inset = False
                if st != -1:
                    if (ed-st) % 2 == 1 and ar[st-1] % 2 == 0 and ar[ed] % 2 == 0:
                        ans = "NO"
                        break
        else:
            if ar[k] % 2 == 1:
                st = k
                inset = True
    """
    print(ans)
                    
