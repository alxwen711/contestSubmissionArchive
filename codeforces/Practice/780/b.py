import sys
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ar.sort()
    if a == 1:
        if ar[0] == 1: print("YES")
        else: print("NO")
    else:
        if ar[-1] <= ar[-2]+1: print("YES")
        else: print("NO")
