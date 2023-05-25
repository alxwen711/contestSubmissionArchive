import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# ?
def solve(n,x):
    if x > n: return "NO"
    while n % 2 == 0:
        n //= 2
    if x % n == 0: return "YES"
    return "NO"

for i in range(readint()):
    n,x = readints()
    # reach x from n
    print(solve(n,x))
