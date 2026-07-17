import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
n = len(s)
h = [0]*26
for i in s:
    h[ord(i)-97] += 1
ans = (n*n-n)//2
f = False
for a in h:
    if a >= 2: f = True
    ans -= (a*a-a)//2
if f: ans += 1
print(ans)
