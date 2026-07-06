import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()

ans = list()
for _ in range(3**n):
    tmp = ["#"]*(3**n)
    ans.append(tmp)
ar = [(0,0,(3**n)//3)]
for _ in range(n):
    br = list()
    for i in ar:
        for a in range(i[2]):
            for b in range(i[2]):
                ans[a+i[0]+i[2]][b+i[1]+i[2]] = "."
        br.append((i[0],i[1],i[2]//3))
        br.append((i[0],i[1]+i[2],i[2]//3))
        br.append((i[0],i[1]+i[2]+i[2],i[2]//3))
        br.append((i[0]+i[2],i[1],i[2]//3))
        br.append((i[0]+i[2],i[1]+i[2]+i[2],i[2]//3))
        br.append((i[0]+i[2]+i[2],i[1],i[2]//3))
        br.append((i[0]+i[2]+i[2],i[1]+i[2],i[2]//3))
        br.append((i[0]+i[2]+i[2],i[1]+i[2]+i[2],i[2]//3))
    ar = br
for c in range(len(ans)):
    print(*ans[c],sep="")
