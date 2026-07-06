import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
#note: cannot remove the entire permutation
"""
1 7 5 4 6 2 3 has a score of 6
2 1 7 4 5 3 6 has a score of 5
n log n bin search the answer?
can fail due to only some scores being possible
index map
"""
def solve(n,ar):
    h = [0]*(n+1)
    for j in range(n):
        h[ar[j]] = j
    score = 1
    low = h[n]
    high = h[n]
    for k in range(n-2):
        x = n-k-1
        xx = h[x]
        low = min(low,xx)
        high = max(high,xx)
        if high-low+1 == k+2: score = k+2
    return score
    
for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
