import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

a = readin()
b = readin()

if a[0] == "A":
    print("Yes" if b[1] != "D" else "No")
if a[1] == "A":
    print("Yes" if b[0] != "D" else "No")
if b[0] == "A":
    print("Yes" if a[1] != "D" else "No")
if b[1] == "A":
    print("Yes" if a[0] != "D" else "No")
