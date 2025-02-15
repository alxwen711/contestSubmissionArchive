import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
11110
0011
"""


for _ in range(readint()):
    n = readint()
    s = readin()
    r = readin()
    a,b = s.count("1"),s.count("0")
    ans = "YES"
    for i in r:
        if a == 0 or b == 0:
            ans = "NO"
            break
        a -= 1
        b -= 1
        if i == "1": a += 1
        else: b += 1
    print(ans)
