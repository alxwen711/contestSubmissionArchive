import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    a,b = 0,n-1
    p = 0
    ans = 0
    c = 0
    for j in range(n):
        if c >= n: break
        aa,bb = ar[a],ar[b]
        if aa < bb: #aa then bb
            if aa >= p:
                ans += 1
                p = aa
                a += 1
            elif bb >= p:
                ans += 1
                p = bb
                b -= 1
            else: 
                a += 1
                b -= 1
                c += 1
        else:
            if bb >= p:
                ans += 1
                p = bb
                b -= 1
            elif aa >= p:
                ans += 1
                p = aa
                a += 1
            else: 
                a += 1
                b -= 1
                c += 1
        c += 1
    print("Case #"+str(i+1)+": "+str(ans))
