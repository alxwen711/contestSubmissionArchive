import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
s = readin()
t = readin()
if s == t: print(0)
else:
    flag = False
    x = min(len(s),len(t))
    for i in range(x):
        if s[i] != t[i]:
            print(i+1)
            flag = True
            break
    if not flag: print(x+1)
