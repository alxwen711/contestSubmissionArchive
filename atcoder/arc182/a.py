import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
either change first p elements to v, or change element p to end to v
all values must go upwards (no decreasing allowed)

n <= 5000, O(n^2) is possible

one of the endpoints is always being covered at minimum

any decrease in v requires a comp check with previous
if the boundaries are possible, some sort of rule is added

answer is always a power of 2


"""

def f(q,ar,br):
    n = len(ar)
    ans = ["?"]*n
    for i in range(n-1):
        for j in range(i+1,n):
            if br[i] > br[j]:
                if ar[i] == ar[j]: return 0
                elif ar[i] < ar[j]: #i -> L, j -> R
                    if ans[i] == "R" or ans[j] == "L": return 0
                    ans[i] = "L"
                    ans[j] = "R"
                else: # i -> R, j -> L
                    if ans[i] == "L" or ans[j] == "R": return 0
                    ans[i] = "R"
                    ans[j] = "L"
    v = 1
    for k in ans:
        if k == "?": v = (v*2) % 998244353
    return v
n,q = readints()
ar = list()
br = list()
for _ in range(q):
    p,v = readints()
    ar.append(p)
    br.append(v)
print(f(q,ar,br))
