import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    for j in range(n):
        br.append([ar[j],j])
    br.sort()
    start = br[0][0]
    ans = list()
    for k in range(1,n):
        if start < br[k][0]:
            start *= ((br[k][0]//start)+1)
        ans.append([br[k][1]+1,start-br[k][0]])
    print(len(ans))
    for m in range(len(ans)):
        print(*ans[m])
    
