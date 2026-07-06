import sys
for i in range(int(sys.stdin.readline())):
    o,e = 0,0
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if ar[j] % 2 == 0: e += 1
        else: o += 1
    print(n-max(o,e))
    
