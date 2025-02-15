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
    ans = sum(ar)
    while len(ar) != 1:
        br = list()
        for i in range(len(ar)-1):
            br.append(ar[i]-ar[i+1])
        ar = br
        ans = max(abs(sum(ar)),ans)
    print(ans)
    
