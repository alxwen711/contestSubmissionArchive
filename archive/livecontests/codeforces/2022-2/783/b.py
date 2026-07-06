import sys
for i in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = sum(ar)+n+max(ar)-min(ar)
    if ans > m: print("NO")
    else: print("YES")
