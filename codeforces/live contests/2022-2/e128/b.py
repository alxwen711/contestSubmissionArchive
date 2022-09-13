import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    ar = list()
    for j in range(a):
        x = str(sys.stdin.readline())
        x = x[:b]
        ar.append(x)
    mx,my = 999,999
    for c in range(a):
        for d in range(b):
            if ar[c][d] == "R":
                if c < mx: mx = c
                if d < my: my = d
    if ar[mx][my] == "R": print("YES")
    else: print("NO")
