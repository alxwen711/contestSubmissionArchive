import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
O(n^2) dp? best using some number of segments?
It really does not feel like a greedy problem
"""


def overlap(a,b):
    if a[1] < b[0] or b[1] < a[0]: return False
    return True

for i in range(readint()):
    n = readint()
    ar = list()
    for nhteou in range(n):
        a,b = readints()
        ar.append([a,b])
    ar.sort()
    br = list()
    for j in range(n):
        tmp = [0]*n
        br.append(tmp)
    for a in range(n):
        for b in range(n):
            if a != b:
                if overlap(ar[a],ar[b]): br[a][b] = 1
    print(ar)
    print(br)
