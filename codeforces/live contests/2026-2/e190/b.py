import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
x12
x24
x32
x44
4

all 4's are removed
any 2's must be at the front of the list;
either remove all in front non 2's
or remove all 2's or some sliding combo
"""

for _ in range(readint()):
    s = readin()
    ar = list()
    ans = 0
    for i in s:
        if i == "4":
            ans += 1
        else:
            ar.append(i)
    v = ar.count("2")
    mv = v
    for u in ar:
        if u == "2": v -= 1
        else: v += 1
        mv = min(v,mv)
    print(ans+mv)
