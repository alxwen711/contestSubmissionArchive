import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,m,k = readints()
    s = readin()
    index = 0
    chain = 0
    ans = 0
    while index < n:
        if s[index] == "0":
            chain += 1
            if chain == m:
                ans += 1
                index += k
                chain = 0
            else:
                index += 1
        else:
            chain = 0
            index += 1
    print(ans)
