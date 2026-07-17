import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
first digit must be a 1

"""
for _ in range(readint()):
    n = readint()
    s = str(n)
    base = s[0]
    ans = "YES"
    for i in range(1,len(s)):
        base += s[i]
        base = int(base)
        if base == 19 and i == len(s)-1:
            ans = "NO"
            break
        elif base == 10 and i != len(s)-1:
            ans = "NO"
            break
        elif base < 10 or base > 19:
            ans = "NO"
            break
        else:
            base = "1"
    print(ans)
    
