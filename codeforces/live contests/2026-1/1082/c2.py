import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
12345322
once this starts decreasing, can only increment by 1,
can decrease by anything up to the start chain val
lengths of chains?

last testcase count:
122333333
-11222222
--1222222
---111111
----11112
-----1112
------112
-------12
--------1

work backwards?
check the latest this value could have come from
"""

def f(n):
    x = 0
    for i in range(1,n+1):
        x += i*(n+1-i)
    return x

for _ in range(readint()):
    n = readint()
    ar = readar()
    prev = 462387463874678364873264783624
    rv = 48762834687326487364
    ans = f(n)
    #cl = 0
    #cr = list()
    d = {}
    index = 0
    br = list()
    for i in ar:
        if i > rv or i <= prev:
            prev = i
            rv = prev+1
            #if cl != 0: cr.append(cl)
            #cl = 0
            d = {}
            d[i] = index
            br.append(index)
        else:
            rv = i+1
            d[i] = index
            br.append(d[i-1]) # this has to exist by rule
        #cl += 1
        index += 1
    ans = f(n)
    for b in range(n):
        if br[b] != b:
            left = br[b]+1
            right = n-b
            ans -= left*right
    print(ans)
