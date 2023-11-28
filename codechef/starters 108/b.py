import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n):
    s = sys.stdin.readline()
    ar = list()
    one = 0
    zero = 0
    for i in range(n):
        ar.append(int(s[i]))
        if ar[-1] == 0: zero += 1
        else: one += 1
    x = 0
    for a in range(n-1,-1,-1):
        if ar[a] == 0: x -= 1
        else: x += 1
        if abs(x) == 2: return "NO"
    return "YES"

for _ in range(readint()):
    n = readint()
    print(solve(n))
