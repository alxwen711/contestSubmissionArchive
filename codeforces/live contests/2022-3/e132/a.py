import sys
for i in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    if ar[x-1] == 0: print("NO")
    else:
        n = ar[x-1]
        if ar[n-1] == 0: print("NO")
        else: print("YES")
