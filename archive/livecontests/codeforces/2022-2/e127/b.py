import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    x = ar[-1]-ar[0]
    if x > n+1: print("NO")
    else: print("YES")
