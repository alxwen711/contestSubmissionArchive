import sys

def solve(n,k,ar):
    if k == 1: return (n-1)//2
    ans = 0
    for j in range(n-2):
        if ar[j+1] > (ar[j]+ar[j+2]): ans += 1
    return ans

for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    print(solve(n,k,ar))
