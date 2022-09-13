import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    x = sum(ar)/len(ar)
    ans = "NO"
    for j in range(len(ar)):
        if ar[j] == x:
            ans = "YES"
            break
    print(ans)
