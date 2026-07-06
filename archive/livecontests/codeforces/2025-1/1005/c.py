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
    ar = readar()
    pos = [0]
    neg = [0]
    for i in range(n):
        pos.append(pos[-1]+max(0,ar[i]))
        neg.append(neg[-1]+max(0,-ar[-i-1]))
    #print(pos)
    #print(neg)
    ans = 0
    for j in range(n+1):
        ans = max(ans,pos[j]+neg[n-j])
    print(ans)
