import sys

for i in range(int(sys.stdin.readline())):
    n,p = map(int,sys.stdin.readline().split())
    a = list()
    b = list()
    ans = 0
    for j in range(n):
        tmp = list(map(int,sys.stdin.readline().split()))
        ta,tb = min(tmp),max(tmp)
        ans += tb-ta
        a.append(ta)
        b.append(tb)
    ar = list()
    for k in range(2):
        tmp = [0]*n
        ar.append(tmp)
    #[0][x] is for choosing low end
    #[1][x] is for choosing high end
    ar[0][0] = a[0]
    ar[1][0] = b[0]
    for m in range(n-1):
        ar[0][m+1] = min(ar[0][m]+abs(b[m]-a[m+1]),ar[1][m]+abs(a[m]-a[m+1]))
        ar[1][m+1] = min(ar[0][m]+abs(b[m]-b[m+1]),ar[1][m]+abs(a[m]-b[m+1]))
    ans += min(ar[0][-1],ar[1][-1])
    print("Case #"+str(i+1)+": "+str(ans))
        
