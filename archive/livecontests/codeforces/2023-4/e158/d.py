import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
consider LT binary
able to choose the target, past that the chain lightning is random
"""

n = readint()
ar = readar()
br = [0]*n #right sec
bv = -1
cr = [0]*n #left sec
cv = -1
for i in range(1,n):
    br[i] = i+ar[i]
    cr[-i-1] = i+ar[-i-1]

bbr = [0]*n
ccr = [0]*n

for bb in range(n-1):
    bv = max(bv,br[-bb-1])
    bbr[bb+1] = bv

for cc in range(n-1):
    cv = max(cv,cr[cc])
    ccr[cc+1] = cv
    
ans = 999999999999999999999999999999
if n == 1: print(ar[0])
else:
    for j in range(1,n-1):
        ans = min(ans,max(ccr[j],ar[j],bbr[n-j-1]))
    ans = min(max(ar[0],bbr[n-1]),ans)
    ans = min(max(ar[-1],ccr[n-1]),ans)
    print(ans)
    
