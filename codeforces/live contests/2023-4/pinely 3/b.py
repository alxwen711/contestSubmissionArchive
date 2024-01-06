import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
01000
01111
10110
11110

00111
"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    b = 2
    #br = list()
    while True:
        br = list()
        for i in ar:
            br.append(i % b)
        if br.count(br[0]) == n:
            b *= 2
        else: break
    print(b)
    
