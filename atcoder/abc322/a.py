import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
s = input()
ans = -1
for i in range(n-2):
    if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
        ans = i+1
        break
print(ans)
