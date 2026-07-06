import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(a,b,c,d):
    if b > d: return -1
    ans = d-b
    x = a + ans
    if x < c: return -1
    return ans+x-c
for i in range(readint()):
    a,b,c,d = readints()
    print(solve(a,b,c,d))
