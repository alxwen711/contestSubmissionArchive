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
n = len(s)
ar = list()
br = list()
for i in range(n):
    if s[i] != t[i]:
        if ord(s[i]) > ord(t[i]): ar.append(i)
        else: br.append(i)
br.reverse()
ans = list()
for a in ar:
    s = s[:a]+t[a]+s[a+1:]
    ans.append(s)
for b in br:
    s = s[:b]+t[b]+s[b+1:]
    ans.append(s)
print(len(ans))
for an in ans:
    print(an)
