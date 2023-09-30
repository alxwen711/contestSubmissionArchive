import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
s = input()
t = input()
pre = True
suf = True
for i in range(n):
    if s[i] != t[i]:
        pre = False
        break
inc = m-n
for j in range(n):
    if s[j] != t[inc+j]:
        suf = False
        break
if pre:
    if suf: print(0)
    else: print(1)
else:
    if suf: print(2)
    else: print(3)
