import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    neg = 0
    for j in range(n):
        if ar[j] < 0:
            neg += 1
            ar[j] = abs(ar[j])
    for k in range(neg):
        ar[k] = ar[k]*(-1)
    ans = "YES"
    for l in range(n-1):
        if ar[l] > ar[l+1]:
            ans = "NO"
            break
    print(ans)
        
    
