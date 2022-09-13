import sys
for i in range(int(sys.stdin.readline())):
    t = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    ans = "NO"
    for j in range(t-1):
        if ar[j] > ar[j+1]:
            ans = "YES"
            break
    print(ans)
