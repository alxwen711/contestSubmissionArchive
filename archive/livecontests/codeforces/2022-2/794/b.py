import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    h = [0]*n
    ans = 0
    for j in range(n-1):
        if ar[j] > ar[j+1] and h[j] == 0 and h[j+1] == 0:
            ans += 1
            h[j] = 1
            h[j+1] = 1
    print(ans)
    
