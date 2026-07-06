import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
))(())())( -2 sum, must be some multiple of 4 to work
(()()()))()(
(()()()()())



)()()((()()(
)()()))()()(

just try to greed?
)(( -< (()
))( -> ())
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    ar = list()
    for i in s:
        ar.append(i)
    x = ar.count("(")-ar.count(")")
    if x % 4 != 0: print(-1)
    else:
        if x > 0:
            for i in range(n-2,-1,-1):
                if x == 0: break
                if x > 0 and ar[i] == "(" and ar[i+1] == "(":
                    ar[i],ar[i+1] = ")",")"
                    x -= 4
        elif x < 0:
            for i in range(n-1):
                if x == 0: break
                if x < 0 and ar[i] == ")" and ar[i+1] == ")":
                    ar[i],ar[i+1] = "(","("
                    x += 4
            
        for i in range(n-2):
            if ar[i:i+3] == [")",")","("]:
                ar[i],ar[i+1],ar[i+2] = "(",")",")"
        for j in range(n-3,-1,-1):
            if ar[i:i+3] == [")","(","("]:
                ar[i],ar[i+1],ar[i+2] = "(","(",")"
        print(*ar,sep="")
