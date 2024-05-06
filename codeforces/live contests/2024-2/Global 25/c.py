import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
greedy time?
"""

def solve(n,m,k,ar):
    br = list()
    for i in range(n):
        br.append((ar[i],i))
    br.sort()
    br.reverse()
    t = [0]*n
    while k > 0: #at most n times
        c = min(m,k)
        t[br[-1][1]] = c
        k -= c
        br.pop()
    ans = 0
    inc = 0
    for a in range(n):
        ans += (ar[a]+inc)*t[a]
        inc += t[a]
    return ans

for _ in range(readint()):
    n,m,k = readints()
    ar = readar()
    print(solve(n,m,k,ar))
