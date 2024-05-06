import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
t = input()

if t[-1] == "X": t = t[:2]
index = 0
ans = "No"
for i in s:
    if index == len(t):
        ans = "Yes"
        break
    if t[index].lower() == i: index += 1

if index == len(t):
    ans = "Yes"
print(ans)
