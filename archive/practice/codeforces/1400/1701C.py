#practice run
import sys

input = sys.stdin.readline

def t(h,n,x,m):
    tasks = 0
    for k in range(n):
        if h[k] >= x: tasks += x
        else:
            tasks += h[k]
            tasks += (x-h[k])//2
        if tasks >= m: return True
    return False


def solve(h,n,m):
    high = 2*m
    low = 1
    while high-low > 1:
        mid = (low+high)//2
        if t(h,n,mid,m): high = mid
        else: low = mid
    if t(h,n,low,m): return low
    else: return high


for i in range(int(input())):
    n,m = map(int,input().split())
    ar = list(map(int,input().split()))
    h = [0]*n
    for j in range(m):
        h[ar[j]-1] += 1
    print(solve(h,n,m))
