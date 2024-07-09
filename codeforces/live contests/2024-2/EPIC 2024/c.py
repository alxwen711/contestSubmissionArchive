import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
compute indiv times for being knocked down
"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.reverse()
    ans = ar[0]
    time = ar[0]
    for i in range(1,n):
        # determine when it would end
        ans = max(ans+1,ar[i])
    print(ans)
        
    
