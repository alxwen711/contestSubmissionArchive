import sys
n,m = map(int,sys.stdin.readline().split())
ar = list(map(int,sys.stdin.readline().split()))
left = [0]*(n)
right = [0]*(n)
s = 0
for j in range(n-1):
    if ar[j] > ar[j+1]: s += (ar[j]-ar[j+1])
    left[j+1] = s
s = 0
for k in range(n-1):
    if ar[n-k-1] > ar[n-k-2]: s += (ar[n-k-1]-ar[n-k-2])
    right[k+1] = s

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if a == b: print(0)
    elif a < b: #left case
        print(left[b-1]-left[a-1])
    else: #right case
        print(right[n-b]-right[n-a])
