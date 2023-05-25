import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(h,n):
    odd = 0
    for snth in range(26):
        if h[snth] == n:
            if n % 2 == 0: return 1
            return 2
        if h[snth] % 2 == 1: odd += 1
    if odd > 1: return 0
    # either 1 odd with odd len or 0 odd with even len
    return 1
    
for i in range(readint()):
    n = readint()
    s = input()
    h = [0]*26
    for j in range(n):
        h[ord(s[j])-97] += 1
    print(solve(h,n))
