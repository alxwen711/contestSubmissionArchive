import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# is this brute forcable

s,t = readins()
ans = "No"
for i in range(1,len(s)):
    for j in range(i):
        x = ""
        for k in range(j,len(s),i):
            x += s[k]
        if x == t:
            ans = "Yes"
            break
    if ans == "Yes": break
print(ans)
