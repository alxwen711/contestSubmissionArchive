import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# x a x x can be allowed

for _ in range(readint()):
    n = readint()
    ar = readar()
    d = {}
    for i in ar:
        if d.get(i) == None:
            d[i] = 0
        d[i] += 1
    highest = 0
    v = -1
    for e in d.keys():
        if d[e] > highest:
            highest = d[e]
            v = e
    ans = sum(ar)
    nothighest = n-highest
    if nothighest+2 < highest: ans -= v*(highest-nothighest-2)
    print(ans)
