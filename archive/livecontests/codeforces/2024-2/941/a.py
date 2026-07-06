import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
1 unique value -> Alice wins
1 x -> Bob wins
x y, x != 1 -> Alice plays x-1 to win
any gap of two gives you option to change chirality
"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    ar = list(set(ar))
    ar.sort()
    ans = 1
    for i in range(len(ar)):
        ans ^= 1
        if ar[i] != i+1: break
    if ans == 1: print("Bob")
    else: print("Alice")
