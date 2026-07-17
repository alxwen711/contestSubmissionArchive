import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
run 3 cycles, after 3rd for future is
arithmetic progression
find first number then there has to
be some sort of dp to get sequential unused
numbers?
"""

def solve(n,k,ar):
    if ar[0] != 1: return 1
    

for i in range(readint()):
    n,k = readints()
    ar = readar()
    print(solve(n,k,ar))
