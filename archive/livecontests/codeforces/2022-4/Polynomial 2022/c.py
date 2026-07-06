import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()



for i in range(readint()):
    n = readint()
    s = input()
    ans = list()
    x = "2"
    chain = 1
    for j in range(n-1):
        if s[j] == x:
            chain += 1
        else:
            chain = 1
            x = s[j]
        ans.append(j+2-chain)
    print(*ans)
