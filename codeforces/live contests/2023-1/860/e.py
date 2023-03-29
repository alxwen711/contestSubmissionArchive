import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
Every array f value is either 0,1,2
2 -> set first to 1, second to m-2
0 -> already valid
1 -> either first is 1 or second is m-2 or somehow almost valid
use previous info to track sets?
If first is 0, then every element before new set is at most 1
0 if counting sets right (first val 3, next val 2, etc.)
if 1 and in error counting sets then same case
track which points result in a number of completed sets
sort of tree structure where a child is in a set??
track what is a perfect fit and how many sets each value has? if valid?
3 4 1 2 1 7 7 3 1 3 1 2 1 1 4 2 7 1 1
4 3 4 3 3 0 2 3 4 0 3 2 2 0 1 0 0 1 0
0 0 1 1 1 1 1 1 1 0 1 0 1 0 2 1 1 1 

"""

def solve(n,ar):
    h = [0]*n
    p = [0]*n
    m = [0]*n
    for i in range(n):
        index = n-i-1
        push = index+ar[index]+1
        if push == n:
            p[index] = 1
            h[index] = 1
        elif push < n:
            if h[push] != 0:
                p[index] = 1
                h[index] = h[push]+1
    m[-1] = h[-1]
    for snth in range(n-1):
        m[-snth-2] = max(h[-snth-2],m[-snth-1])
    print(h)
    print(m)
    ans = [0]*(n-1)
    for j in range(n-1):
        if ar[j] == h[j+1]: ans[j] = 0
        elif h[j+1] != 0: ans[j] = 1
        elif ar[j] == 1: ans[j] = 1
        elif m[j+1]+1 >= ar[j]: ans[j] = 1 #this line is a problem
        else: ans[j] = 2
    print(*ans)

for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
