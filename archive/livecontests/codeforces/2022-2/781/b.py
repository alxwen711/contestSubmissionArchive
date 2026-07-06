import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    d = {}
    for j in range(len(ar)):
        if d.get(ar[j]) == None: d[ar[j]] = 1
        else: d[ar[j]] += 1
    k = max(list(d.values()))
    diff = n - k
    ans = 0
    while diff != 0:
        ans += 1
        if 2*k >= n: break
        ans += k
        k += k
    ans += n-k
    print(ans)
        
