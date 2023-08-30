import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
cover downwards effect
go row by row, counting total number of affected from above
O(n^2) is possible
"""


def solve(n,ar):
    st = [0]*n
    ed = [0]*n
    inc = 0
    ans = 0
    for a in range(n):
        for b in range(n):
            plus = False
            inc += st[b]
            if (inc+ar[a][b]) % 2 == 1: plus = True
            inc -= ed[b]
            if plus:
                ans += 1
                st[b] += 1
                ed[b] += 1
        # adjust increments
        for c in range(1,n):
            st[c-1] += st[c]
            st[c] = 0
        for d in range(n-1):
            ed[-d-1] += ed[-d-2]
            ed[-d-2] = 0
    return ans
                

for i in range(readint()):
    n = readint()
    ar = list()
    for j in range(n):
        s = sys.stdin.readline()
        tmp = list()
        for k in range(n):
            tmp.append(int(s[k]))
        ar.append(tmp)
    print(solve(n,ar))
