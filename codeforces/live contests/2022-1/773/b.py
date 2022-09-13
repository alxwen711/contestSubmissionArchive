import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = 0
    ar.sort()
    prev = 74379572934875
    for j in range(n):
        if ar[j] != prev:
            prev = ar[j]
            ans += 1
    for l in range(ans):
        print(ans,end=" ")
    for m in range(n-ans):
        print(ans+m+1,end=" ")
    print()
