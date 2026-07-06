import sys

for i in range(int(sys.stdin.readline())):
    l = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    h = [0]*100
    ans = 0
    if ar.count(0) != 0: ans += 1
    for j in range(len(ar)):
        if ar[j] != 0: h[abs(ar[j])-1] += 1
    for k in range(100):
        ans += min(2,h[k])
    print(ans)
    
