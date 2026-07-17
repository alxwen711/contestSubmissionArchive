import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
m = readin()
r = [0]*n
p = [0]*n
s = [0]*n
if m[0] == "R": p[0] = 1
elif m[0] == "P": s[0] = 1
else: r[0] = 1

for i in range(1,n):
    if m[i-1] == "R": # R or P last move
        if m[i] == "R":
            r[i] = p[i-1]
            p[i] = r[i-1]+1
        elif m[i] == "P":
            p[i] = r[i-1]
            s[i] = max(r[i-1],p[i-1])+1
        else:
            s[i] = max(r[i-1],p[i-1])
            r[i] = p[i-1]+1
    elif m[i-1] == "P": # P or S last move
        if m[i] == "R":
            r[i] = max(p[i-1],s[i-1])
            p[i] = s[i-1]+1
        elif m[i] == "P":
            p[i] = s[i-1]
            s[i] = p[i-1]+1
        else:
            s[i] = p[i-1]
            r[i] = max(p[i-1],s[i-1])+1
    else: # S or R last move
        if m[i] == "R":
            r[i] = s[i-1]
            p[i] = max(r[i-1],s[i-1])+1
        elif m[i] == "P":
            p[i] = max(r[i-1],s[i-1])
            s[i] = r[i-1]+1
        else:
            s[i] = r[i-1]
            r[i] = s[i-1]+1
print(max(r[-1],p[-1],s[-1]))
