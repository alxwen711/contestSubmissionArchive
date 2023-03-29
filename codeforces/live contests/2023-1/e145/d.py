import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(s):
    a = s.count("0")
    b = s.count("1")
    best = min(a,b)*1000000000001
    l0,l1 = 0,0
    r0,r1 = a,b
    for i in range(len(s)-1):
        if s[i] == "0":
            l0 += 1
            r0 -= 1
        else:
            l1 += 1
            r1 -= 1
        score = (l1+r0)*1000000000001
        if s[i] == "1" and s[i+1] == "0":
            score -= 2000000000002
            score += 1000000000000
        if score < best: best = score
    return best

for i in range(readint()):
    print(solve(input()))
