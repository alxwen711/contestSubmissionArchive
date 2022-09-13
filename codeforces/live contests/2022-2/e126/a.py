import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    br = list(map(int,sys.stdin.readline().split()))
    ans = 0
    for j in range(len(ar)-1):
        if (abs(br[j+1]-ar[j])+abs(ar[j+1]-br[j])) < (abs(ar[j+1]-ar[j]) + abs(br[j+1]-br[j])):
            tmp = ar[j+1]
            ar[j+1] = br[j+1]
            br[j+1] = tmp
        ans += (abs(ar[j+1]-ar[j]) + abs(br[j+1]-br[j]))
    print(ans)
