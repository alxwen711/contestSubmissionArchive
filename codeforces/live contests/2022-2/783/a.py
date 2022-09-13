import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    if a == 1:
        if b <= 2:
            print(b-1)
        else: print(-1)
    elif b == 1:
        if a <= 2:
            print(a-1)
        else: print(-1)
    else:
        ans = 2*max(a-1,b-1)
        if a % 2 != b % 2: ans -= 1
        print(ans)
    
