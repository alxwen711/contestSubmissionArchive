import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
3 unique chars in a row
2 of the same back to back
"""

for _ in range(readint()):
    s = readin()
    n = len(s)
    ans = "-1"
    for i in range(n-1):
        if s[i] == s[i+1]:
            ans = s[i]+s[i+1]
            break
    if ans == "-1":
        for j in range(n-2):
            if s[j] != s[j+1] and s[j+2] != s[j+1] and s[j] != s[j+2]:
                ans = s[j]+s[j+1]+s[j+2]
                break
    print(ans)
