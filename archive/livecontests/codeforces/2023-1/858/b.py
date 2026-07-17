import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#(imagine reading correctly, couldn't be me (runtime error = wrong answer apparently))
def solve(n,ar):
    h = [0,0]
    for i in range(n):
        if ar[i] == 0: h[0] += 1
        elif ar[i] == 1: h[1] += 1
        
    if h[0] <= (n+1)//2: return 0
    elif (h[0]+h[1]) == n and h[1] != 0: return 2
    return 1

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
