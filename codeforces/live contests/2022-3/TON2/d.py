import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
2+6+12+7+8 = 35
2+3+4+10+16 = 35
2+6+6+14+8 = 36
"""

for i in range(readint()):
    n,r = readints()
    ans = list()
    index = 0
    base = 0
    done = False
    for j in range(3):
        ar = readar()
        h = 0
        for k in range(r):
            h += k*ar[k]
        ans.append(h)
    for m in range(3):
        if ans.count(ans[m]) == 1:
            ans = ans[m]-ans[(m+1)%3]
            index = m+1
            done = True
            break
        elif ans.count(ans[m]) == 3:
            base = ans[m]
            break
    for w in range(n-3):
        ar = readar()
        if not done:
            h = 0
            for kk in range(r):
                h += kk*ar[kk]
            if h != base:
                done = True
                ans = h-base
                index = w+4
    print(index,ans)
