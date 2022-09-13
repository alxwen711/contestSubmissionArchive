import sys
for i in range(int(sys.stdin.readline())):
    c = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ans = ar[0] | ar[1]
    
    for j in range(len(ar)-2):
        ans = ans | ar[j+2]
    print(ans)
