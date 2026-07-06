import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
odd case: abababa
even case: ababab
idea is to balance out a/b as closely as possible?
odd case ranges from even to a2, end at a1
odd case is just even case with forced a
even case ranges from b1 to a1, end at 0
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    if n % 2 == 1:
        if s[0] == "b":
            print("NO")
            continue
        s = s[1:]
        n -= 1
    # solve even case
    ans = "YES"
    for i in range(n//2):
        if (s[2*i] == "a" and s[2*i+1] == "a") or (s[2*i] == "b" and s[2*i+1] == "b"):
            ans = "NO"
            break
    print(ans)
