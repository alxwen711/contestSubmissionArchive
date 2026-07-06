import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
emulatable since n is at most 500
k = 1 -> pseudo bubble sort
r-l > k is possible, does not need to = k
O(n^3) is viable
"""

def debug(n,k,ar):
    m = readint()
    for _ in range(m):
        print(*ar)
        a,b = readints()
        a -= 1
        b -= 1
        ar[a],ar[b] = ar[b],ar[a]
    print(*ar)


n,k = readints() # k is min distance requirement
ar = readar()

debug(n,k,ar)
