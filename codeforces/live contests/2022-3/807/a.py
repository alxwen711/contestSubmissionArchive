import sys
input = sys.stdin.readline
for i in range(int(input())):
    n,k = map(int,input().split())
    ar = list(map(int,input().split()))
    ar.sort()
    ans = "YES"
    for j in range(n):
        if ar[j] + k > ar[j+n]:
            ans = "NO"
            break
    print(ans)
