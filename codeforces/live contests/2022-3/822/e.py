import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
need some sort of n log n idea, splitting the array?
making smaller versions then combining them?


2x2
3x3

evenxeven -> 4 n//2 grids, restrict values to range to prevent cross grid fault
oddxodd -> 4 n//2 grids + cross
"""

n = readint()
dia = readar()
ar = list()
for i in range(n):
    ar.append([0]*n)
    ar[i][i] = dia[i]
    for j in range(n):
        ar[i][j] = (abs(j-i)+dia[i]) % n
        
if n == 2 and ar[0][0] == ar[1][1]: ar[1][0] = (ar[1][0]+1) % 2

for snth in range(n):
    print(*ar[snth])
