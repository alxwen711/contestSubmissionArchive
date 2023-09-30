import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

m = 1000000007

for i in range(readint()):
    n = readint()
    s = input()
    ans = 1
    for j in range(n//2):
        a = int(s[2*j])
        b = int(s[2*j+1])
        c = int(s[2*j+2])
        choices = 0
        if a ^ b == c: choices += 1
        if a | b == c: choices += 1
        if a & b == c: choices += 1
        ans = (ans*choices) % m
    print(ans)
