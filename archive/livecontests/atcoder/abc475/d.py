import sys
from itertools import permutations

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
more efficient to brute force the combinations

0 is not prime
"""

s = readin()
ans = -1

letterorder = list()

for i in s:
    if i not in letterorder:
        letterorder.append(i)

u = len(letterorder)

digits = [0,1,2,3,4,5,6,7,8,9]

for p in permutations(digits,u):
    if p[0] == 0: continue # not allowed
    d = {}
    for ii in range(u):
        d[letterorder[ii]] = p[ii]
    v = 0
    for l in s:
        v *= 10
        v += d[l]

    # determine if prime
    if v > 1:
        div = 2
        flag = True
        while div*div <= v:
            if v % div == 0:
                flag = False
                break
            div += 1
        if flag:
            ans = v
            break
print(ans)


    
