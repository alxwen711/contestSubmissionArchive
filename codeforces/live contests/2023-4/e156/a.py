import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n):
    for a in range(1,n-2):
        for b in range(a+1,n):
            c = n-a-b
            if c > 0 and a % 3 != 0 and b % 3 != 0 and c % 3 != 0 and a != c and a != b and c != b:
                return a,b,c
    return -1,-1,-1

for i in range(readint()):
    n = readint()
    a,b,c = solve(n)
    if a == -1: print("NO")
    else:
        print("YES")
        print(a,b,c)
    
