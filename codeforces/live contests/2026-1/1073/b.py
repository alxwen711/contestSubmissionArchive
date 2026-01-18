import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
prefix step is simple?
subsequence -> any position can be removed, could do this greedily
(())() -> (()) (nope)
(()()) -> (()) (nope)
((()())) -> ((())) (no)
(())(()) -> (()()) (yes)

()(()) -> (()) (yes)

(()(())) -> ((()))

"""

for _ in range(readint()):
    n = readint()
    s = readin()
    l,r = list(),list()
    ans = -1
    t = 0
    for i in range(n):
        if s[i] == "(":
            l.append(i)
            t += 1
        else:
            r.append(i)
            t -= 1
        #if t == 0 and i != n-1: ans = i+1
    #print(l,r)
    # determine earliest step of greedy that works
    if n > 2:
        r.reverse()
        for _ in range(n//2-1):
            li,ri = l.pop(),r.pop()
            if l[-1] > ri:
                ans = max(ans,len(l)*2)
                break
    print(ans)
