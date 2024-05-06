import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
h = [0]*26
for i in s:
    h[ord(i)-97] += 1
d = [0]*101
for u in h:
    d[u] += 1
ans = "Yes"
for e in range(1,101):
    if d[e] != 0 and d[e] != 2:
        ans = "No"
        break
print(ans)
