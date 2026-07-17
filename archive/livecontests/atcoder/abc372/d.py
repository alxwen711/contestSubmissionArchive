import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = readar()
ar.reverse()

ans = [0]
lis = [ar[0]]
for i in range(1,n):
    ans.append(len(lis))
    low = 0
    high = len(lis)-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[i] > lis[mid]: high = mid
        else: low = mid
    if ar[i] > lis[low]: lis[low] = ar[i]
    elif ar[i] > lis[high]: lis[high] = ar[i]
    else: lis.append(ar[i])
    while lis[-1] != ar[i]:
        lis.pop()
ans.reverse()
print(*ans)

