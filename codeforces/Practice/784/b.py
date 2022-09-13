import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ar.sort()
    found = False
    for j in range(max(n-2,0)):
        if ar[j] == ar[j+1] == ar[j+2]:
            print(ar[j])
            found = True
            break
    if not found: print(-1)
