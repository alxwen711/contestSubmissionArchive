import sys
for i in range(int(sys.stdin.readline())):
    n,z = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = 0
    for j in range(n):
        ans = max(ans,(z|ar[j]))
    print(ans)
