import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(a,b,c,d):
    if a == 0: return 1
    ans = a
    sta,stb = a,a
    x = min(b,c)
    ans += x*2
    b -= x
    c -= x
    if b != 0:
        if b > stb:
            ans += stb+1
            return ans
        ans += b
        sta += b
        stb -= b
    if c != 0:
        if c > sta:
            ans += sta+1
            return ans
        ans += c
        sta -= c
        stb += c
    ans += min(d,sta+1,stb+1)
    return ans

for i in range(readint()):
    a,b,c,d = readints()
    print(solve(a,b,c,d))
