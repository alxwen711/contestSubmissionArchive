import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# bot if not on position x and reaching then may repeat


def t(p,n,s):
    pos = p
    if s[0] == "L": pos -= 1
    else: pos += 1
    for i in range(1,n):
        if pos == 0: return i
        if s[i] == "L": pos -= 1
        else: pos += 1
    if pos == 0: return n
    return -1
for _ in range(readint()):
    n,x,k = readints()
    s = readin()
    start = t(x,n,s)
    if start == -1 or start > k: print(0)
    else:
        rt = k-start
        tt = t(0,n,s)
        if tt == -1: print(1)
        else: print(1+rt//tt)
