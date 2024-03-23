import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
n*n square, min squares needed for k diagonals to have coloured square
2*2 -> 2,4,5,6
3*3 -> 2,4,6,8,9,10
4*4 -> 2,4,6,8,10,12,13,14
"""
for _ in range(readint()):
    n,k = readints()
    if k == 4*n-2: print(2*n)
    elif k == 4*n-3: print(2*n-1)
    else: print((k+1)//2)
