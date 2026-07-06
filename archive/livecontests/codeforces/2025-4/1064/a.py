import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
always merge smallest?

1145141
145441
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    for i in range(n):
        br.append(max(ar[i],ar[(i+1) % n]))
    print(sum(br)-max(br))
