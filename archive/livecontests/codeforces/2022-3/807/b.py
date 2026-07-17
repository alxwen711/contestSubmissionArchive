import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ar.pop(-1)
    zero = False
    ans = 0
    for j in range(n-1):
        if ar[j] != 0:
            zero = True
            ans += ar[j]
        elif zero: ans += 1
    print(ans)
