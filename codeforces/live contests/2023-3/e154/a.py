import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(s):
    for i in range(9):
        x = int(s[i])
        if x == 1: return 19
        elif x == 3: return 31
        elif x == 5: return 53
        elif x == 7: return 71
        elif x == 9: return 97

for i in range(readint()):
    s = sys.stdin.readline()
    print(solve(s))
