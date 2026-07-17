import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,s):
    if n % 2 == 1:
        print(-1)
        return
    x = 0
    l = list()
    r = list()
    one = True
    pos = False
    for i in range(n):
        if s[i] == "(":
            x += 1
            l.append(i)
        else:
            x -= 1
            r.append(i)
        if x < 0: one = False
        if x > 0: pos = True
    if x != 0:
        print(-1)
        return
    ans = [1]*n
    if pos and (not one):
        print(2)
        for j in range(n//2):
            if r[j] < l[-j-1]:
                ans[r[j]] = 2
                ans[l[-j-1]] = 2
            else: break
    else: print(1)
    print(*ans)


for i in range(readint()):
    n = readint()
    s = sys.stdin.readline()[:-1]
    solve(n,s)
