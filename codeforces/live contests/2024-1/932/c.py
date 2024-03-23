import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
optimal message reading order is from lowest to highest b val
O(n**2) dp
2000+1999*2+1998*3+1997*4
keep current score and highest

current setup would need to test at multiple starting points, still O(n**3)

now a limited O(n**3), about n**3/8 but still feels too slow
"""
"""
for _ in range(readint()):
    n,l = readints()
    ar = list()
    for _ in range(n):
        a,b = readints()
        ar.append((b,a))
    ar.sort()
    da = [0]*n
    db = [0]*n
    da[0] = ar[0][1]
    db[0] = ar[0][0]
    for i in range(1,n):
        a,b = ar[i][1],ar[i][0]
        db[i] = b
        da[i] = da[i-1]+a+b-db[i-1]
        for j in range(i-1,-1,-1): #overwrite better options
            if j == 0:
                if da[0] >= a:
                    da[0] = a
                    db[0] = 0
            else:
                score = da[j-1]+a+b-db[j-1]
                if score <= da[j]:
                    da[j] = score
                    db[j] = b
    ans = 0
    for f in da:
        if f <= l: ans += 1
    print(ans)
    print(da)
"""


for _ in range(readint()):
    n,l = readints()
    ar = list()
    for _ in range(n):
        a,b = readints()
        ar.append((b,a))
    ar.sort()
    dp = list()
    for _ in range(n):
        tmp = [999999999999999999999]*n
        dp.append(tmp)
    for ii in range(n):
        dp[0][ii] = ar[ii][1]
    ans = 0
    if min(dp[0]) <= l:
        ans += 1
        for i in range(1,n):
            for j in range(i,n):
                cost = ar[j][1]
                pos = ar[j][0]
                for k in range(j):
                    dp[i][j] = min(dp[i][j],dp[i-1][k]+cost+pos-ar[k][0])
            if min(dp[i]) <= l: ans += 1
            else: break
    print(ans)
