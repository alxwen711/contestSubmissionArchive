import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(a,n):
    if len(a) == 0: return 10000000000000000
    prev = -1
    b = list()
    for ii in range(len(a)):
        b.append(a[ii]-prev-1)
        prev = a[ii]
    b.append(n-prev-1)
    c = max(b)
    ans = 0
    while c != 0:
        ans += 1
        c = c // 2
    return ans

    
for i in range(readint()):
    s = input()
    h = list()
    n = len(s)
    for htnhtn in range(26):
        h.append(list())
    for j in range(n):
        h[ord(s[j])-97].append(j)
    best = 10000000000000000
    for k in range(26):
        best = min(best,solve(h[k],n))
    print(best)
