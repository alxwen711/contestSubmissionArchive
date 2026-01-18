import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
change 11...00 -> 00...11


101010 -> 001011
011010

110101 -> 010111 (alice wins in one move)
101101 -> 001111

win in one move or lose?
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    ar = list()
    for i in s:
        ar.append(int(i))
    o = sum(ar)
    if sum(ar[n-o:n]) == o: print("Bob") # no moves
    else: # assume that Alice wins
        zero = list()
        one = list()
        for ii in range(n):
            if ar[ii] == 0: zero.append(ii)
            else: one.append(ii)
        req = o-sum(ar[n-o:n])
        ans = list()
        for u in range(req):
            ans.append(one[u]+1)
            ans.append(zero[-u-1]+1)
        ans.sort()
        print("Alice")
        print(len(ans))
        print(*ans)
