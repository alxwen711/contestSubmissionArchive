import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
answer is 1 or 2
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    ar = list()
    br = list()
    for i in s:
        ar.append(i)
        br.append(i)
    ans = 1
    br.sort()
    if ar == br: ans = 2
    br.reverse()
    if ar == br: ans = 2
    if ar.count("0") == 0 or ar.count("1") == 0: ans = 1
    print(ans)
