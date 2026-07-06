import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# delete first ( and last )

for _ in range(readint()):
    s = readin()
    n = len(s)
    count = n//2
    lv = False
    ar = list()
    for i in s:
        if i == "(":
            if lv: ar.append(i)
            else: lv = True
        else:
            count -= 1
            if count != 0: ar.append(i)
    sc = 0
    ans = "NO"
    for j in ar:
        if j == "(": sc += 1
        else: sc -= 1
        if sc < 0:
            ans = "YES"
            break
    print(ans)
