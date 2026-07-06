import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,b,c = readints()
    # x | b - x & a
    """
    represent a and b in bin, compare bits
    for each bit 4 cases:
    a = 0, b = 0 -> x's bit must be 1
    a = 0, b = 1 -> x's bit can be either
    a = 1, b = 0 -> x's bit can be either
    a = 1, b = 1 -> x's bit must be 0
    """
    ans = 1
    ar = list()
    br = list()
    while a != 0 or b != 0:
        ar.append(a % 2)
        br.append(b % 2)
        a //= 2
        b //= 2
    for n in range(min(len(ar),len(br))):
        if ar[n] != br[n]: ans *= 2
    print(ans)
