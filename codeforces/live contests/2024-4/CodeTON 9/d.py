import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
elements will be repeated
a1 cannot equal any other value
a2 cannot equal any second value
a3 cannot equal any third value
...

"""

def solve(n,m,ar):
    ans = list()
    ans.append(0)
    ar.sort()
    ar.reverse()
    for i in range(1,n):
        h = [1]*min(m,150)
        v = i+1
        c = 1
        while c*c < v:
            if v % c == 0:
                h[ans[c-1]] = 0
                if c != 1:
                    h[ans[v//c-1]] = 0
            c += 1
        if c*c == v:
            h[ans[c-1]] = 0
        flag = True
        for j in range(len(h)):
            if h[j] == 1:
                ans.append(j)
                flag = False
                break
        if flag:
            print(-1)
            return
    bans = list()
    for snth in ans:
        bans.append(ar[snth])
    print(*bans)
        
for _ in range(readint()):
    n,m = readints()
    ar = readar()
    solve(n,m,ar)
    
    
