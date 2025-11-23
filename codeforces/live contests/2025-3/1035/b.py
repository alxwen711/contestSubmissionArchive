import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    a,b,c,d = readints()
    ar = readar()
    madist = sum(ar)
    h = max(ar)
    midist = h-(madist-h)
    dv = (a-c)**2+(b-d)**2
    if madist*madist < dv: print("No")
    elif midist <= 0 or midist*midist <= dv: print("Yes")
    else: print("No")
