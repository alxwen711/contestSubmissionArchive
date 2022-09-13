import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        ar[j] = ar[j] % 2
    a,b = ar[0],ar[1]
    ans = "YES"
    for k in range(n-2):
        if k % 2 == 0:
            if ar[k+2] != a:
                ans = "NO"
                break
        if k % 2 == 1:
            if ar[k+2] != b:
                ans = "NO"
                break
    print(ans)
