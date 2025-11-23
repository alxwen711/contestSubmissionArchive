import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

ar = readar()
ans = "No"
for i in range(1,14):
    for j in range(1,14):
        if i != j and ar.count(i) >= 3 and ar.count(j) >= 2:
            ans = "Yes"
            break
print(ans)
