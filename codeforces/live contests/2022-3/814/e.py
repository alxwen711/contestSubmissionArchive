import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    s = sum(ar)
    if s == 1: return "YES"
    elif s == 2:
        if len(ar) == 2: return "YES"
        else: return "NO"
    elif s == 3: return "NO"
    fib = list()
    fib.append(1)
    fib.append(1)
    c = 2
    while c < s:
        y = fib[-1]+fib[-2]
        fib.append(y)
        c += y
    if c != s: return "NO"
    fib.reverse()
    prev = 8572985789237
    for j in range(len(fib)):
        xx = fib[j]
        index = -1
        highest = 0
        for k in range(n):
            if ar[k] > highest and k != prev:
                highest = ar[k]
                index = k
        if highest < xx: return "NO"
        else:
            #print(index)
            ar[index] -= xx
            prev = index
    return "YES"


for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
