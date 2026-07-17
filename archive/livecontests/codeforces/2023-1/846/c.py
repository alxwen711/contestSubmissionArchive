import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1
13 4
1 1 1 1 1 1 1 1 1 2 2 2 2
3 3 3 5

Solution fails on this testcase, turns out this question is NP-Hard
can be compared to 3-parition problem/knapsack

"""
for i in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar()
    br.sort()
    br.reverse()
    h = [0]*(n+1)
    for j in range(n):
        h[ar[j]] += 1
    p = [0]*(n+1)
    high = 0
    for k in range(n+1):
        if h[k] != 0:
            high = max(high,h[k])
            p[h[k]] += 1
    ans = 0
    for l in range(m):
        if high == 0: break
        x = br[l]
        if x > high: #use high
            ans += high
            p[high] -= 1
        elif p[x] != 0: #use fit
            ans += x
            p[x] -= 1
        else: #use high
            ans += x
            p[high] -= 1
            p[high-x] += 1
        if p[high] == 0: #reset top
            while p[high] == 0 and high > 0:
                high -= 1
    print(ans)
