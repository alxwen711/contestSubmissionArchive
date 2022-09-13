import sys

def peak(ar,x,n):
    if x <= 0 or x >= n-1: return False
    if ar[x] > ar[x-1] and ar[x] > ar[x+1]: return True
    else: return False

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for j in range(n-2):
        if peak(ar,j+1,n): #ar[j+1] is peak
            if peak(ar,j+3,n):
                ar[j+2] = max(ar[j+1],ar[j+3])
            else:
                ar[j+2] = ar[j+1]
            ans += 1
    print(ans)
    for k in range(n):
        print(ar[k],end=" ")
    print()
