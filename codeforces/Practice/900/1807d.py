import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,q = readints()
    ar = readar()
    dp = [0]*n
    dp[0] = ar[0]
    for j in range(1,n):
        dp[j] = ar[j] + dp[j-1]
    t = dp[-1] #total sum
    for k in range(q):
        l,r,x = readints()
        v = t-dp[r-1]
        if l != 1: v += dp[l-2]
        v += (r-l+1)*x
        print("YES" if v % 2 == 1 else "NO")
