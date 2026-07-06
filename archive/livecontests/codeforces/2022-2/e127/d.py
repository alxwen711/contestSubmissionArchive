import sys
for i in range(int(sys.stdin.readline())):
    n,x = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = 0
    for j in range(n-1):
        ans += abs(ar[j]-ar[j+1])
    a,b = min(ar),max(ar)
    if a > 1:
        ans += min(ar[0]-1,ar[n-1]-1,(a-1)*2)
    if b < x:
        ans += min(x-ar[0],x-ar[n-1],(x-b)*2)
    print(ans)
        
