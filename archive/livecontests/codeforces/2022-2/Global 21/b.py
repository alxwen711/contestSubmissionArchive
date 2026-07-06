import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    o = True
    ans = 0
    for j in range(n):
        if o:
            if ar[j] != 0:
                o = False
                ans += 1
        else:
            if ar[j] == 0:
                o = True
        if ans == 2: break
    print(ans)
