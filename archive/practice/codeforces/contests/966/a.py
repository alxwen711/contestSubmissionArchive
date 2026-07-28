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
    s = str(n)
    if len(s) <= 2: print("NO")
    elif s[:2] != "10": print("NO")
    elif str(int(s[2:])) != s[2:]: print("NO")
    elif int(s[2:]) < 2: print("NO")
    else: print("YES")
