import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
nxn grid
1 2 3
4 5 6
7 8 9
"""

n,t = readints()
ar = readar()
rows = [0]*n
cols = [0]*n
d1 = 0
d2 = 0
ans = -1
for i in range(t):
    x = ar[i]-1
    r,c = x//n,x%n
    rows[r] += 1
    if rows[r] == n:
        ans = i+1
        break
    cols[c] += 1
    if cols[c] == n:
        ans = i+1
        break
    if r == c:
        d1 += 1
        if d1 == n:
            ans = i+1
            break
    if r+c == n-1:
        d2 += 1
        if d2 == n:
            ans = i+1
            break
print(ans)
    
