import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = 0
    o,e = 0,0
    if n % 2 == 0: #even case
        br = [0]*(n//2)
        cr = [0]*(n//2)
        bi,ci = 1,1
        for k in range(1,n-1,2):    
            if not (ar[k] > ar[k-1] and ar[k] > ar[k+1]):
                o += ((max(ar[k-1],ar[k+1])+1)-ar[k])
            br[bi] = o #cost for 1 cool building with left fix
            bi += 1
        ar.reverse()
        for m in range(1,n-1,2):
            if not (ar[m] > ar[m-1] and ar[m] > ar[m+1]):
                e += ((max(ar[m-1],ar[m+1])+1)-ar[m])
            cr[ci] = e #right fix
            ci += 1
            
        ans = min(o,e) #no fix
        for w in range(n//2):
            ans = min(ans,br[w]+cr[-w-1])
        
    else:
        for j in range(1,n-1,2):
            if not (ar[j] > ar[j-1] and ar[j] > ar[j+1]):
                ans += ((max(ar[j-1],ar[j+1])+1)-ar[j])
    print(ans)         
