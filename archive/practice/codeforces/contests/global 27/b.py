import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
must be length n
if dividing 66, then 33 passes
66 = 11*2*3
last digit must be a 6
is the answer 33333....33336366?
"""

for _ in range(readint()):
    n = readint()
    if n == 1: print(-1)
    elif n == 2: print(66)
    elif n == 3: print(-1)
    elif n % 2 == 1: print("3"*(n-4)+"6366")
    else: print("3"*(n-2)+"66")
    
