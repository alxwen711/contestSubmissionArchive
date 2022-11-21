import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def freq_ar(ar: list, limit: int) -> list:
    if ar == None: return []
    h = [0]*limit #change to limit+1 for h[1] = freq of 1
    for i in range(len(ar)):
        h[ar[i]-1] += 1 #change to h[ar[i]] for h[1] = freq of 1
    return h


def solve(n,ar):
    h = freq_ar(ar,n)
    a = 0
    for i in range(len(h)):
        if h[i] != 0: a += 1
    if a > 2: return n
    if a == 1: return 1
    return n//2+1


for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
