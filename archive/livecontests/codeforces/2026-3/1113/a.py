import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    s = readin()
    z,o = True,True
    ans = list()
    for i in s:
        if i == "0":
            if z: z = False
            else: ans.append(i)
        else:
            if o: o = False
            else: ans.append(i)
    print(*ans,sep="")
