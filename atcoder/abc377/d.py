import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
l r indicates
for starting points 1 to l, must end at r-1 or earlier

"""

n,m = readints()
mv = [99999999999999]
for i in range(1,m+1):
    mv.append(m)
for _ in range(n):
    l,r = readints()
    mv[l] = min(r-1,mv[l])
ma = 99999999999999999
ans = 0
#print(mv)
for j in range(m,0,-1):
    ma = min(mv[j],ma)
    #print(ans,ma,j)
    ans += (ma-j+1)
    
print(ans)
