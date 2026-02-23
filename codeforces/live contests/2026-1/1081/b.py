import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1000 -> hold 0's (0's must be odd)
1111 -> hold 1's
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    c = 0
    for i in range(n):
        c += int(s[i])
    if c == 0: print(0)
    elif c % 2 == 1:
        if (n-c) % 2 == 0: print(-1)
        else:
            ans = list()
            for j in range(n):
                if s[j] == "0": ans.append(j+1)
            print(len(ans))
            print(*ans)
    else:
        ans = list()
        for j in range(n):
            if s[j] == "1": ans.append(j+1)
        print(len(ans))
        print(*ans)
        
