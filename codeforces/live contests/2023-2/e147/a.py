import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = input()
    ans = 1
    if n[0] == "?": ans *= 9
    elif n[0] == "0": ans *= 0
    for j in range(1,len(n)):
        if n[j] == "?": ans *= 10
    print(ans)
