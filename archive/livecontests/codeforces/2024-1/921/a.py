import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
greedily choose the last letter possible not covered
abc...z*26 is a full cover
"""

for _ in range(readint()):
    n,k,m = readints()
    s = sys.stdin.readline()
    ans = list()
    d = [1]*k
    r = k
    for i in range(m):
        x = ord(s[i])-97
        if d[x] == 1:
            r -= 1
            d[x] = 0
            if r == 0:
                ans.append(chr(x+97))
                if len(ans) == n:
                    break
                d = [1]*k
                r = k
    if len(ans) == n: print("YES")
    else:
        print("NO")
        for j in range(k):
            if d[j] == 1:
                ans.append(chr(j+97))
                break
        while len(ans) != n:
            ans.append("a")
        print(*ans,sep="")
