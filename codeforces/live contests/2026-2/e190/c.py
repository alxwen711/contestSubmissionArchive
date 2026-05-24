import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
every chain is at least length 2
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    indiv = 0
    boost = 0
    ans = 0
    br = list()
    for i in ar:
        if i == 1: indiv += 1
        else:
            ans += i
            boost += (i-2)//2
            br.append(i)
    if len(br) == 1: boost += 1
    ans += min(boost,indiv)
    if ans < 3: print(0)
    else: print(ans)
