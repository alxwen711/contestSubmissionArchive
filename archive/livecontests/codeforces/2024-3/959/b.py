import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
first digit is 1 -> can change everything else as necessary, yes
first digit is 0 ->


01 -> 00
10 -> 11 -> 01 -> 00

00010
"""
for _ in range(readint()):
    n = readint()
    s = readin()
    t = readin()
    if s[0] == "0" and t[0] == "1": print("NO")
    elif s[0] == "0" and t[0] == "0":
        flag = True
        for i in range(1,n):
            if s[i] == "1": break
            if t[i] == "1":
                flag = False
                break
        if flag: print("YES")
        else: print("NO")
    else: print("YES")
