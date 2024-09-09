import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
do not see too many colours being required
only need to xor check with primes

18k primes

4-colouring in theory should always work?

1 2 3 4 1 2 3 4 1 2 3 4
"""

for _ in range(readint()):
    n = readint()
    if n == 1:
        print(1)
        print("1")
    elif n == 2:
        print(2)
        print("1 2")
    elif n == 3:
        print(2)
        print("1 2 2")
    elif n == 4:
        print(3)
        print("1 2 2 3")
    elif n == 5:
        print(3)
        print("1 2 2 3 3")
    else:
        print(4)
        ar = list()
        for i in range(n):
            ar.append(i % 4 + 1)
        print(*ar)
    
