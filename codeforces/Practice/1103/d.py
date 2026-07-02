import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Each successive element must be same or up to k higher than previous
A goal is to setup E with guaranteed last move
There can be multiple at the highest

1 4 7
if 1 is a win, 7 is a win and this is rendered moot

determine all end states where single value is repeatedly chosen
if even case, pull a win out there
if odd case, check if something within k exists
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    d = [0]*(n+1)
    br = list()
    for i in ar:
        if d[i] == 0:
            br.append(i)
        d[i] += 1
    br.sort()
    ans = "NO"
    for a in range(len(br)-1):
        if br[a]+k < br[a+1]: # possible endpoint
            if d[br[a]] % 2 == 0:
                ans = "YES"
                break
            elif a != 0 and br[a-1]+k >= br[a]:
                ans = "YES"
                break
    # check the last one
    if d[br[-1]] % 2 == 0:
        ans = "YES"
    elif len(br) != 1 and br[-2]+k >= br[-1]:
        ans = "YES"
    print(ans)
