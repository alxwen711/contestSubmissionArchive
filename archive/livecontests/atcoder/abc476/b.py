import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
s = readin()
t = readin()
ans = "Yes"
for i in range(n):
    if t[i] != "*" and s[i] != t[i]:
        ans = "No"
        break
print(ans)
