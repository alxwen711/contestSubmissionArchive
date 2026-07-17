import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    ans = list()
    h = [0]*(n+3)
    for i in ar:
        h[i] += 1
    s = n
    while s != 0:
        index = 0
        while h[index] != 0:
            h[index] -= 1
            index += 1
        if index == 0: break
        else:
            s -= index
            ans.append(index)
    for j in range(s):
        ans.append(0)
    print(len(ans))
    print(*ans)

for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
