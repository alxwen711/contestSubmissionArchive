import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n % 2 == 0: print(n//2,0,0)
    else: print(-1)
