import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
C1 is O(n^2)
C2 is O(n log n)

x tables with m seats each
I -> if empty table exists, add there
E -> if non empty table exists, add there
A -> ternary search on number of first A to set to empty tables?
"""

def f(s,x,m,i):
    # set first i A's to empty
    a,b = x,0
    ans = 0
    for p in s:
        if p == "I":
            if a != 0:
                ans += 1
                a -= 1
                b += m-1
        elif p == "E":
            if b != 0:
                ans += 1
                b -= 1
        else:
            if i != 0 and a != 0:
                a -= 1
                b += m-1
                ans += 1
                i -= 1
            elif b != 0:
                ans += 1
                b -= 1
    return ans


for _ in range(readint()):
    n,x,m = readints()
    s = readin()
    ans = 0
    low = 0
    high = x
    while high-low > 50:
        diff = high-low
        mid1 = low+diff//3
        mid2 = low+(diff*2)//3
        m1 = f(s,x,m,mid1)
        m2 = f(s,x,m,mid2)
        if m1 >= m2: high = mid2
        if m1 <= m2: low = mid1
    for ii in range(low,high+1):
        ans = max(ans,f(s,x,m,ii))
    print(ans)
