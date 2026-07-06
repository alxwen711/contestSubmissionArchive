import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
4      1
8 3
3 2/4 ? 8 5 6 7 1
8 8
8 2 3 4 5 6 7 1
8 4
4 2 3 8 5 6 7 1
100 23

8 2
2 4 3 8 5 6 7 1

6 2
2 6 3 4 5 1

12 2
2 4 3 12 5 6 7 8 9 10 11 1

16 2
2 4 3 8 5 6 7 16 9 10 11 12 13 14 15 1
"""

def solve(n,x):
    if n % x != 0:
        print(-1)
        return
    ans = list()
    ans.append(n)
    for i in range(n-2):
        ans.append(i+2)
    ans.append(1)
    if n == x:
        print(*ans)
        return
    ans[0] = x
    ans[x-1] = n
    swap = x-1
    for j in range(x,n//2):
        if n % (j+1) == 0 and (j+1) % (swap+1) == 0:
            ans[swap] = j+1
            ans[j] = n
            swap = j
    print(*ans)
    return

for i in range(readint()):
    n,x = readints()
    solve(n,x)
