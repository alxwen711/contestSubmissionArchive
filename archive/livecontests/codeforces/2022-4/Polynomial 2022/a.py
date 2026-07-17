import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    x = input()
    s = int(x[0])
    ans = list()
    for j in range(1,n):
        if x[j] == "1":
            if s == 1:
                s = 0
                ans.append("-")
            else:
                s = 1
                ans.append("+")
        else:
            ans.append("+")
    print(*ans,sep="")
