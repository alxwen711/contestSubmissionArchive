import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
count the number that do have it as a subsequence?
substring count, no modulo indicated
at each starting point, greedy choose closest
"""

s = readin()
t = readin()

n,m = len(s),len(t)

h = [n]*26
ar = list()
for i in range(n-1,-1,-1):
    h[ord(s[i])-97] = i
    ar.append(deepcopy(h))
ar.reverse()

bcode = list()
for b in t:
    bcode.append(ord(b)-97)

ans = 0
for j in range(n):
    sp = j
    for c in range(m):
        vpos = ar[sp][bcode[c]]
        if c != m-1:
            if sp == vpos: sp += 1
            else: sp = vpos+1
        else:
            if sp == vpos: sp = sp
            else: sp = vpos
        if sp >= n:
            sp = n
            break
    ans += sp-j
print(ans)
