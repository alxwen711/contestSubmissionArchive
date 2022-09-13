import sys
for i in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x % 2 == 1: print(0)
    else:
        ans = 1
        for j in range(x//2):
            ans *= (j+1)
        print((ans*ans)%998244353)
    
