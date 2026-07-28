import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
inside selection is allowed
just keep matching first and last together?
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    s = readin()
    prefix = [0]
    for i in ar:
        prefix.append(prefix[-1]+i)
    l,r = 0,n-1
    ans = 0
    while l < r:
        while l != n:
            if s[l] == "L": break
            l += 1
        if l == n: break
        while r != -1:
            if s[r] == "R": break
            r -= 1
        if r == -1: break
        if l >= r: break

        ans += prefix[r+1]-prefix[l]
        l += 1
        r -= 1
    print(ans)
